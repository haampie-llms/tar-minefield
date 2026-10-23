// List the members of a tar archive with Go's archive/tar, as JSON, for contrib/matrix/matrix.py.
//
//	go run . ARCHIVE
//
// prints {"members": [...]} or, if the reader returns an error, {"members": [...], "error": "..."}
// with the members before it. archive/tar has no extractor: programs apply the members themselves.
package main

import (
	"archive/tar"
	"crypto/sha256"
	"encoding/hex"
	"encoding/json"
	"io"
	"os"
)

type member struct {
	Name     string `json:"name"`
	Type     string `json:"type"`
	Size     int64  `json:"size"`
	Linkname string `json:"linkname,omitempty"`
	Sha256   string `json:"sha256,omitempty"`
}

func main() {
	f, err := os.Open(os.Args[1])
	if err != nil {
		panic(err)
	}
	r := tar.NewReader(f)
	out := struct {
		Members []member `json:"members"`
		Error   string   `json:"error,omitempty"`
	}{Members: []member{}}
	for {
		h, err := r.Next()
		if err == io.EOF {
			break
		}
		if err != nil {
			out.Error = err.Error()
			break
		}
		m := member{Name: h.Name, Type: string([]byte{h.Typeflag}), Size: h.Size, Linkname: h.Linkname}
		if h.Typeflag == tar.TypeReg || h.Typeflag == tar.TypeRegA {
			s := sha256.New()
			if _, err := io.Copy(s, r); err != nil {
				out.Members = append(out.Members, m)
				out.Error = err.Error()
				break
			}
			m.Sha256 = hex.EncodeToString(s.Sum(nil))
		}
		out.Members = append(out.Members, m)
	}
	json.NewEncoder(os.Stdout).Encode(out)
}
