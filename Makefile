#          Makefile for rfmodbuslib tasks
#
# ----------------------------------------------------------------------------
#
# Note that this is a GNU Makefile.
# nmake and other abominations are not supported.
#
# ----------------------------------------------------------------------------

ifndef SILENCE
	SILENCE = @
endif

define HELP

 smartsecurity makefile help
 ---------------------------

 Please use `make <target>' where <target> is one of:

  --- build commands
  install          install lib and dependencies

  --- documentation commands
  doc              build keywords documentation

endef
export HELP

NAME = $(shell PYTHONPATH=. python -c "import rfmodbuslib; print rfmodbuslib.__lib_name__")
VERSION = $(shell PYTHONPATH=. python -c "import rfmodbuslib; print rfmodbuslib.__lib_version__")
GIT_HASH = $(shell git log -1 --format=%h)
DOC_DIR = doc

.PHONY: help clean install doc

# keep this rule first
help:
	@echo "$$HELP"

clean: clean-bytecode clean-egg clean-doc

clean-bytecode:
	@echo "Cleaning byte code..."
	$(SILENCE)find -name \*.py[co] -exec rm {} \;

clean-egg:
	@echo "Cleaning python eggs..."
	$(SILENCE)rm -rf *.egg-info
	$(SILENCE)rm -rf build
	$(SILENCE)rm -rf dist

install:
	@echo "Installing package..."
	python setup.py install

# PYTHONPATH has to be set for doc subdir for users who do not have it set
DOC_ARGS = PYTHONPATH=../..

doc: doc-html
	@echo "Built $(NAME) doc for version $(VERSION) [$(GIT_HASH)]"

doc-html:
	@echo "Building keywords documentation (html)..."
	$(SILENCE)make -C $(DOC_DIR) $(DOC_ARGS) html
	@echo "Done."
	@echo "Please, open the following link with your favorite web browser:"
	@echo $(CURDIR)/$(DOC_DIR)/build/html/index.html

clean-doc:
	@echo "Cleaning docs..."
	$(SILENCE)make -C $(DOC_DIR) $(DOC_ARGS) clean
	@echo "Done."
