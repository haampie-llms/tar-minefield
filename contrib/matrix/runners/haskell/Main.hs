{-# LANGUAGE CPP #-}
-- | Extract a tar archive with the tar package's extract, which reads, checks for paths outside
-- the destination, and unpacks, for contrib/matrix/matrix.py.
--
-- > runner ARCHIVE DEST
--
-- An error is printed on stderr, with status 1. With --version, prints the versions.
module Main (main) where

import qualified Codec.Archive.Tar as Tar
import Control.Exception (SomeException, try)
import Data.Version (showVersion)
import System.Environment (getArgs)
import System.Exit (ExitCode (..), exitWith)
import System.IO (hPutStrLn, stderr)
import System.Info (compilerVersion)

main :: IO ()
main = do
  args <- getArgs
  case args of
    ["--version"] ->
      putStrLn ("tar " ++ VERSION_tar ++ ", extract, of GHC " ++ showVersion compilerVersion)
    [archive, dest] -> do
      result <- try (Tar.extract dest archive) :: IO (Either SomeException ())
      either (\e -> hPutStrLn stderr (show e) >> exitWith (ExitFailure 1)) return result
    _ -> hPutStrLn stderr "usage: runner ARCHIVE DEST" >> exitWith (ExitFailure 2)
