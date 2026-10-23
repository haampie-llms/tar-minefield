// Extract a tar archive with the unpack of a Rust tar library, for contrib/matrix/matrix.py.
//
//     runner tar|astral-tokio-tar|tar-codec-uv ARCHIVE DEST
//
// exits with status 1 and the error on stderr if unpack fails.
fn main() {
    let args: Vec<String> = std::env::args().collect();
    let (library, archive, dest) = (args[1].as_str(), &args[2], &args[3]);
    let result: Result<(), String> = match library {
        "tar" => {
            let file = std::fs::File::open(archive).expect("open");
            tar::Archive::new(file).unpack(dest).map_err(|e| e.to_string())
        }
        // tar-codec with the policies that uv 0.13 sets, in crates/uv-extract/src/stream.rs
        "tar-codec-uv" => {
            use tar_codec::extract::{ExtractPolicy, LinkPolicy};
            use tar_codec::{
                Archive as _, DecodePolicy, PaxDecodePolicy, PaxVendorExtensionPolicy, TarArchive,
            };
            let decode_policy = DecodePolicy::default()
                .allow_header_uname_and_gname_without_terminator(true)
                .pax_policy(
                    PaxDecodePolicy::default()
                        .vendor_extension_policy(PaxVendorExtensionPolicy::ignore([
                            "SCHILY",
                            "LIBARCHIVE",
                        ]))
                        .allow_non_utf8_pax_vendor_values(true),
                );
            let extract_policy =
                ExtractPolicy::default().link_policy(LinkPolicy::default().allow_hard_links(true));
            let runtime = tokio::runtime::Builder::new_current_thread().build().unwrap();
            runtime.block_on(async {
                let file = tokio::fs::File::open(archive).await.expect("open");
                TarArchive::new(file)
                    .with_policy(decode_policy)
                    .extract_in(dest, extract_policy)
                    .await
                    .map_err(|e| e.to_string())
            })
        }
        _ => {
            let runtime = tokio::runtime::Builder::new_current_thread().build().unwrap();
            runtime.block_on(async {
                let file = tokio::fs::File::open(archive).await.expect("open");
                tokio_tar::Archive::new(file).unpack(dest).await.map_err(|e| e.to_string())
            })
        }
    };
    if let Err(e) = result {
        eprintln!("{e}");
        std::process::exit(1);
    }
}
