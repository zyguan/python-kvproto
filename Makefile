UNAME 	:= $(shell uname)
SED	:= sed -i

ifeq ($(UNAME), Darwin)
	SED := gsed -i
endif

gen-imports = for f in $$(find kvproto/rev_$(2) -name '*.py' | sort); do name=$$(basename $$f .py); [ $$name == __init__ ] || echo from kvproto.rev_$(2) import $$name >> $(1); done

gen-kvproto: \
	kvproto/release_30.py \
	kvproto/release_31.py \
	kvproto/release_40.py \
	kvproto/master.py

kvproto/master.py: gen-kvproto-f7ca9b5 FORCE
	rm -f $@ && echo '# DO NOT EDIT THIS FILE BY HAND' > $@
	$(call gen-imports,$@,$(subst gen-kvproto-,,$<))

kvproto/release_30.py: gen-kvproto-e53d835 FORCE
	rm -f $@ && echo '# DO NOT EDIT THIS FILE BY HAND' > $@
	$(call gen-imports,$@,$(subst gen-kvproto-,,$<))

kvproto/release_31.py: gen-kvproto-c211b47 FORCE
	rm -f $@ && echo '# DO NOT EDIT THIS FILE BY HAND' > $@
	$(call gen-imports,$@,$(subst gen-kvproto-,,$<))

kvproto/release_40.py: gen-kvproto-3500763 FORCE
	rm -f $@ && echo '# DO NOT EDIT THIS FILE BY HAND' > $@
	$(call gen-imports,$@,$(subst gen-kvproto-,,$<))

gen-kvproto-%:
	cd .gen/kvproto/ && make kvproto_$*/prepare
	python -m grpc_tools.protoc --python_out=. --grpc_python_out=. \
		-I.gen/kvproto/kvproto_$* .gen/kvproto/kvproto_$*/kvproto/rev_$*/*.proto
	$(SED) 's,/kvproto\.rev_$*\.,/,' kvproto/rev_$*/*_grpc.py
	touch kvproto/rev_$*/__init__.py

FORCE:

.PHONY: FORCE
