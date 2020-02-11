UNAME := $(shell uname)
SED	  := sed -i

ifeq ($(UNAME), Darwin)
	SED := gsed -i
endif

kvproto_%/prepare: pingcap-kvproto-%.tar.gz
	mkdir -p $(dir $@)kvproto/rev_$*
	rm -f $(dir $@)kvproto/rev_$*/*
	tar -xf $<
	cp -r pingcap-kvproto-$*/proto/* $(dir $@)kvproto/rev_$*/
	cp -r pingcap-kvproto-$*/include/google $(dir $@) || true
	cp -r pingcap-kvproto-$*/include/eraftpb.proto $(dir $@)kvproto/rev_$*/ || true
	$(SED) 's/\(^\(import\|option\).\+\(gogoproto\|rustproto\)\)/\/\/ \1/' $(dir $@)kvproto/rev_$*/*.proto
	$(SED) 's/ \+\(\[.*gogoproto.*\]\)/ \/\*\1\*\//g' $(dir $@)kvproto/rev_$*/*.proto
	$(SED) 's/^import "google/__IMPORT_GOOGLE__/' $(dir $@)kvproto/rev_$*/*.proto
	$(SED) 's/^import "/import "kvproto\/rev_$*\//' $(dir $@)kvproto/rev_$*/*.proto
	$(SED) 's/^__IMPORT_GOOGLE__/import "google/' $(dir $@)kvproto/rev_$*/*.proto
	$(SED) 's/^package \(.\+\);/package  kvproto.rev_$*.\1;/' $(dir $@)kvproto/rev_$*/*.proto

pingcap-kvproto-%.tar.gz:
	wget -O $@ https://api.github.com/repos/pingcap/kvproto/tarball/$*

.PRECIOUS: pingcap-kvproto-%.tar.gz
