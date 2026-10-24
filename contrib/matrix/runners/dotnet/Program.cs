// Extract a tar archive with System.Formats.Tar's TarFile.ExtractToDirectory, for
// contrib/matrix/matrix.py. overwriteFiles is false, as in the example of its documentation.
//
//     runner ARCHIVE DEST
//
// An error is printed on stderr, with status 1. With --version, prints the version of .NET.
using System.Formats.Tar;
using System.Runtime.InteropServices;

if (args is ["--version"])
{
    Console.WriteLine($"System.Formats.Tar of {RuntimeInformation.FrameworkDescription}, ExtractToDirectory");
    return 0;
}
try
{
    TarFile.ExtractToDirectory(args[0], args[1], overwriteFiles: false);
    return 0;
}
catch (Exception e)
{
    Console.Error.WriteLine($"{e.GetType().Name}: {e.Message}");
    return 1;
}
