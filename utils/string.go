package utils

import (
	"strings"
)

func SingleLeading(s string, ch string) string {
	/*
	Examples
	/ 		-> /
	// 		-> /
	/a/ 	-> /a
	/a/b/d 	-> /a/b/d
	a/b 	-> /a/b
	/a/b/ 	-> /a/b
	a/b/ 	-> /a/b
	*/
	s = strings.Trim(s, ch)
	s = ch + s
	return s
}

func SingleLeadingTrailing(s string, ch string) string {
	/*
	Examples
	/ 		-> /
	// 		-> /
	/a/ 	-> /a/
	/a/b/d 	-> /a/b/d/
	a/b 	-> /a/b/
	/a/b/ 	-> /a/b/
	a/b/ 	-> /a/b/
	*/
	s = strings.Trim(s, ch)
	s = strings.TrimRight(ch + s, ch)
	s = s + ch
	return s
}

func JoinLeading(s1 string, s2 string, ch string) string {
	s1 = strings.Trim(s1, ch)
	s2 = strings.Trim(s2, ch)
	s := s1 + ch + s2
	return SingleLeading(s, ch)
}

func JoinLeadingTrailing(s1 string, s2 string, ch string) string {
	s1 = strings.Trim(s1, ch)
	s2 = strings.Trim(s2, ch)
	s := s1 + ch + s2
	return SingleLeadingTrailing(s, ch)
}
