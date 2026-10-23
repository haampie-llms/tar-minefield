// Extract a tar archive with the unpack of a Rust tar library, for corpus/matrix.py.
//
//     runner tar|astral-tokio-tar ARCHIVE DEST
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
