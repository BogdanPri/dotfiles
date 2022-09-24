;;; $DOOMDIR/config.el -*- lexical-binding: t; -*-

;; Place your private configuration here! Remember, you do not need to run 'doom
;; sync' after modifying this file!


;; Some functionality uses this to identify you, e.g. GPG configuration, email
;; clients, file templates and snippets. It is optional.

(setq user-full-name "Bogdan Pricope"
      user-mail-address "bogdan.pricope6198@gmail.com")

;; Doom exposes five (optional) variables for controlling fonts in Doom:
;;
;; - `doom-font' -- the primary font to use
;; - `doom-variable-pitch-font' -- a non-monospace font (where applicable)
;; - `doom-big-font' -- used for `doom-big-font-mode'; use this for
;;   presentations or streaming.
;; - `doom-unicode-font' -- for unicode glyphs
;; - `doom-serif-font' -- for the `fixed-pitch-serif' face
;;
;; See 'C-h v doom-font' for documentation and more examples of what they
;; accept. For example:
;;
;;(setq doom-font (font-spec :family "Fira Code" :size 12 :weight 'semi-light)
;;      doom-variable-pitch-font (font-spec :family "Fira Sans" :size 13))

(setq doom-font (font-spec :family "Hack Nerd Font Mono" :size 15)
      doom-unicode-font (font-spec :family "MesloLGS NF" :size 15))

(after! unicode-fonts
  (let ((doom-font-name (plist-get
                         (font-face-attributes doom-font) :family)))
    (dolist (unicode-fonts-fallback-font
             (list doom-font-name))
      (add-to-list 'unicode-fonts-fallback-font-list unicode-fonts-fallback-font))
    (dolist (unicode-block '("Cyrillic"
                             "Cyrillic Extended-A"
                             "Cyrillic Extended-B"
                             "Cyrillic Supplement"

                             "Greek Extended"
                             "Greek and Coptic"))
      (push doom-font-name (cadr (assoc unicode-block unicode-fonts-block-font-mapping))))
    ))

;; If you or Emacs can't find your font, use 'M-x describe-font' to look them
;; up, `M-x eval-region' to execute elisp code, and 'M-x doom/reload-font' to
;; refresh your font settings. If Emacs still can't find your font, it likely
;; wasn't installed correctly. Font issues are rarely Doom issues!

;; There are two ways to load a theme. Both assume the theme is installed and
;; available. You can either set `doom-theme' or manually load a theme with the
;; `load-theme' function. This is the default:
(setq doom-theme 'doom-dracula)
(add-to-list 'default-frame-alist '(alpha . 90))

;; This determines the style of line numbers in effect. If set to `nil', line
;; numbers are disabled. For relative line numbers, set this to `relative'.
(setq display-line-numbers-type 'relative)

;; If you use `org' and don't want your org files in the default location below,
;; change `org-directory'. It must be set before org loads!
(setq org-directory "~/Documents/dev/org/"
      org-agenda-files '("~/Documents/dev/org/agenda/agenda.org")
      org-ellipsis " ▼ "
      org-default-notes-file (expand-file-name "notes.org" org-directory)
      org-log-done 'time
      org-journal-dir "~/Documents/dev/org/journal/"
      org-journal-date-format "%B %d, %Y (%A) "
      org-journal-file-format "%Y-%m-%d.org"
      org-hide-emphasis-markers t)
(setq org-src-preserve-indentation nil
      org-src-tab-acts-natively t
      org-edit-src-content-indentation 0)

;; Whenever you reconfigure a package, make sure to wrap your config in an
;; `after!' block, otherwise Doom's defaults may override your settings. E.g.
;;
;;   (after! PACKAGE
;;     (setq x y))
;;
;; The exceptions to this rule:
;;
;;   - Setting file/directory variables (like `org-directory')
;;   - Setting variables which explicitly tell you to set them before their
;;     package is loaded (see 'C-h v VARIABLE' to look up their documentation).
;;   - Setting doom variables (which start with 'doom-' or '+').
;;
;; Here are some additional functions/macros that will help you configure Doom.
;;
;; - `load!' for loading external *.el files relative to this one
;; - `use-package!' for configuring packages
;; - `after!' for running code after a package has loaded
;; - `add-load-path!' for adding directories to the `load-path', relative to
;;   this file. Emacs searches the `load-path' when you load packages with
;;   `require' or `use-package'.
;; - `map!' for binding new keys
;;
;; To get information about any of these functions/macros, move the cursor over
;; the highlighted symbol at press 'K' (non-evil users must press 'C-c c k').
;; This will open documentation for it, including demos of how they are used.
;; Alternatively, use `C-h o' to look up a symbol (functions, variables, faces,
;; etc).
;;
;; You can also try 'gd' (or 'C-c c d') to jump to their definition and see how
;; they are implemented.

;; Makes the 's' key behave like in vim.
(remove-hook 'doom-first-input-hook #'evil-snipe-mode)

;; Sets up 'flyspell' to use the en_GB mode.
(autoload 'flyspell-babel-setup "flyspell-babel")
(add-hook 'latex-mode-hook 'flyspell-babel-setup)
(setq ispell-program-name "hunspell")
(setq ispell-local-dictionary "en_GB")
(setq ispell-local-dictionary-alist
      '(("en_GB" "[[:alpha:]]" "[^[:alpha:]]" "[']" nil nil nil utf-8)))
(require 'python)
(load "auctex.el" nil t t)
(add-hook 'LaTeX-mode-hook 'flyspell-mode)
(add-hook 'python-mode-hook 'flyspell-prog-mode)

;; Setting 'dired' keys
(evil-define-key 'normal dired-mode-map
  (kbd "h") 'dired-up-directory
  (kbd "l") 'dired-find-file)

(use-package all-the-icons)

(use-package emojify
  :hook (after-init . global-emojify-mode))

(use-package org-bullets)
(add-hook 'org-mode-hook (lambda () (org-bullets-mode 1)))

(use-package gcmh
  :config
  (gcmh-mode 1))
(setq gc-cons-threshold 402653184
      gc-cons-percentage 0.6)

(use-package unicode-fonts)

(setq auto-mode-alist (cons '("\\.\\(pde\\|ino\\)$" . arduino-mode) auto-mode-alist))
(autoload 'arduino-mode "arduino-mode" "Arduino editing mode." t)

;; (use-package gnuplot)

(org-babel-do-load-languages
 'org-babel-load-languages '((C . t)
                             (gnuplot . t)
                             (matlab . t)))

;; mu4e setup
(use-package mu4e
  :config
  (setq mu4e-change-filenames-when-moving t)
  (setq mu4e-update-interval (* 10 60))
  (setq mu4e-get-mail-command "mbsync -a")
  (setq mu4e-maildir "~/.mail")

  (setq mu4e-drafts-folder "/[Gmail].Drafts")
  (setq mu4e-sent-folder "/[Gmail].Sent Mail")
  (setq mu4e-refile-folder "/[Gmail].All Mail")
  (setq mu4e-trash-folder "/[Gmail].Trash")

  (setq mu4e-maildir-shortcuts
        '(("/Inbox"             . ?i)
          ("/[Gmail].Sent Mail" . ?s)
          ("/[Gmail].Trash"     . ?t)
          ("/[Gmail].Drafts"    . ?d)
          ("/[Gmail].All Mail"  . ?a))))
;; (defun my-matlab-hook ()
;;   (mlint-minor-mode 1))
;; (add-hook 'matlab-mode-hook 'my-matlab-hook)
