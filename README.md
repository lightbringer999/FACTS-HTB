# FACTS-HTB
Hacthebox Season 10’s first Easy Linux machine exploits a path traversal in Camaleon CMS to read the user flag and SSH private key (id_rsa). Using the key, we log in via SSH. Then, abusing the Ruby-based facter binary and custom directories, we execute commands as root and obtain the root flag. This repo contains all required files.
