// Extract a tar archive with containerd's archive.Apply, which applies the layers of container
// images, for contrib/matrix/matrix.py. It reads with Go's archive/tar, and has its own handling of
// paths, links, existing entries and whiteouts. WithNoSameOwner, as the archives are owned by root
// and ownership is not part of the trees that matrix.py compares.
//
//	runner ARCHIVE DEST
//
// An error is printed on stderr, with status 1. With --version, prints the versions.
package main

import (
	"context"
	"fmt"
	"os"
	"runtime"
	"runtime/debug"

	"github.com/containerd/containerd/v2/pkg/archive"
)

func main() {
	if len(os.Args) == 2 && os.Args[1] == "--version" {
		version := "?"
		if info, ok := debug.ReadBuildInfo(); ok {
			for _, dep := range info.Deps {
				if dep.Path == "github.com/containerd/containerd/v2" {
					version = dep.Version
				}
			}
		}
		fmt.Printf("containerd %s, archive.Apply, of %s\n", version, runtime.Version())
		return
	}
	f, err := os.Open(os.Args[1])
	if err != nil {
		fmt.Fprintln(os.Stderr, err)
		os.Exit(1)
	}
	if _, err := archive.Apply(context.Background(), os.Args[2], f, archive.WithNoSameOwner()); err != nil {
		fmt.Fprintln(os.Stderr, err)
		os.Exit(1)
	}
}
