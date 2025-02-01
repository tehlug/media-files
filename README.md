# Tip for clone specific directory that you wish to
If you only want to clone a specific subdirectory of a Git repository, you can use the `--depth` and `--filter` options with the `git clone` command. Here's an example:
```bash
git clone --depth 1 --filter=blob:none --sparse git@github.com:tehlug/media-files.git && \
cd media-files && \
git sparse-checkout init --cone && \
git sparse-checkout set events/images/<event_number>
```
