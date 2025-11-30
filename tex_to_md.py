#!/usr/bin/env python3
import re

def tex_to_markdown(tex_path, md_path):
    with open(tex_path, 'r', encoding='utf-8') as f:
        tex = f.read()

    # Remove comments
    tex = re.sub(r'%.*', '', tex)

    # Replace sections
    tex = re.sub(r'\\CVSection\{([^}]*)\}', r'\n## \1\n', tex)
    tex = re.sub(r'\\cvheading\{([^}]*)\}\{([^}]*)\}', r'# \1\n**\2**\n', tex)
    tex = re.sub(r'\\cvsubheading\{([^}]*)\}', r'\n\1\n', tex)

    # Experience items
    tex = re.sub(r'\\CVItem\[(.*?)\]\{(.*?)\}\{', r'### \2 — \1\n', tex)

    # Bullets
    tex = tex.replace(r'\begin{itemize}', '')
    tex = tex.replace(r'\end{itemize}', '')
    tex = tex.replace(r'\item', '-')

    # Simple cleanup
    tex = tex.replace('\\hfill', '')
    tex = re.sub(r'\\[a-zA-Z]+', '', tex)  # remove remaining commands
    tex = re.sub(r'\{|\}', '', tex)

    # Remove extra whitespace
    lines = [line.rstrip() for line in tex.split('\n') if line.strip()]
    md_output = '\n'.join(lines)

    with open(md_path, 'w', encoding='utf-8') as f:
        f.write(md_output)

    print(f"Markdown resume saved to {md_path}")


# Example usage:
# tex_to_markdown("resume.tex", "resume.md")
if __name__ == "__main__":
    tex_to_markdown("resume.tex", "resume.md")
