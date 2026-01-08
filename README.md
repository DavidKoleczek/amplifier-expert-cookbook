# Amplifier Expert Cookbook

Expert examples and reusable workflows for Amplifier. This repository contains multiple bundles that can be loaded independently.

## Available Bundles

### cli-tool-builder

Multi-stage CLI application development with capability reconnaissance, pilot implementations, and iterative building.

**Installation:**
```bash
amplifier bundle add git+https://github.com/DavidKoleczek/amplifier-expert-cookbook@main#subdirectory=cli-tool-builder
amplifier bundle use cli-tool-builder
```

**Usage:**
```bash
# Interactive
amplifier run
> Run the cli-tool-development recipe with cli_description: "Build a CLI tool that..."

# Non-interactive
amplifier recipes execute cli-tool-builder:recipes/cli-tool-development.yaml \
  --context '{"cli_description": "Build a CLI tool that..."}'
```

See [cli-tool-builder/README.md](cli-tool-builder/README.md) for detailed documentation.

## Adding More Bundles

To add a new bundle to this cookbook:

1. Create a new directory: `my-bundle/`
2. Add `bundle.md` with YAML frontmatter and instructions
3. Add `README.md` with human documentation
4. Add context files in `context/` and recipes in `recipes/` as needed

## License

MIT
