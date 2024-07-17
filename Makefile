# Copyright (C) ALbert Mietus, SoftwareBeterMaken.nl; 2017-2019,2023 Part of my MESS project
default: html

docs_TARGETS =	html
docs: 		${docs_TARGETS}
all: 		docs run_pytests

DOCd          =  .
OUTd          =  __result/
TMPd	     ?=  tmp/
SPHINX_CACHE  =  ${TMPd}sphinx_cache


##
## User-friendly check for sphinx-build
##
SPHINXBUILD   = sphinx-build
ifeq ($(shell which $(SPHINXBUILD) >/dev/null 2>&1; echo $$?), 1)
  $(error The '$(SPHINXBUILD)' command was not found. Make sure you selected a "Python3" (virt)env with Sphinx installed)
endif

##
## Pass make option to sphinx-build
##
ifneq (,$(findstring B,$(MAKEFLAGS)))
  build_opts+=-a -E
endif
ifneq (,$(findstring J,$(MAKEFLAGS)))
  build_opts+=-j
endif


SPHINX_OPTS = ${build_opts} -d ${SPHINX_CACHE}

${docs_TARGETS}:
	${PYTHONPATH} $(SPHINXBUILD) -q -c ${DOCd} -b $@ ${SPHINX_OPTS}  ${DOCd} ${OUTd}$@
	@echo "Build finished, See: ${OUTd}$@"

clean:
	rm -rf ${SPHINX_CACHE}

cleaner veryclean: clean
	rm -rf ${OUTd}*
	rm -rf `find . -type d -name __pycache__`

cleanest: cleaner; #nothing extra


run_pytests::
	-(cd pyMESS/training/dPID/; pytest)
	@echo "NOTE: One Assert is to be expected (AssertionError in test_clip) -- ignoring"

HOGSMEADEd = /Volumes/albert/Sites/MESS/

Hogsmeade_check: # Is `~albert` on Hogsmeade mounted?
	@echo -n Checking ${HOGSMEADEd} ...
	@[ -d ${HOGSMEADEd} ]
	@echo ok

Hogsmeade: Hogsmeade_check
	${MAKE} OUTd=${HOGSMEADEd}

Hogsmeade-clean: Hogsmeade_check
	${MAKE} OUTd=${HOGSMEADEd} cleanest

#include RTD-settings.mk
#RTD  RTfD-build RTfD RTFD RTfD-webhook:
#	-hg push
#	@BRANCH=$${BRANCH:-`hg branch`} ;\
#	curl -X POST -d "branches=$${BRANCH}" -d "token=${TOKEN}"  ${HOOK}
#	@echo

RTD:
	-hg push
	-hg bookmarks default
	-hg push github
	@echo "push to github will trigger RTD"


wc:
	@echo "lines	words	file"
	@wc -lw `find . -iname \*rst`|sort -r | grep -v /index.rst | grep -v /zz.todo.rst

