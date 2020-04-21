;; Install required packages if not installed.
(mapc #'(lambda (package)
  (unless (package-installed-p package)
    (package-install package)))
    '(elpy poetry tox)
)

;; Elpy for python development.
(require 'elpy)
(elpy-enable)
(setenv "WORKON_HOME" "~/.virtualenvs")

;; Set python version to use.
(setq py-python-command 'python3)

;; Set python version for elpy.
(setq python-shell-interpreter "python3"
      python-shell-interpreter-args "-i")
(setq elpy-test-runner (quote elpy-test-pytest-runner))

;; Tox.
(setq tox-runner 'py.test-3)

;; Default enviroment for running tox (same as tox.ini).
(defvar tox-default-env "py37" "Default argument for Tox")

;; Poetry.
(require 'poetry)
