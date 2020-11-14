# Aprenda OpenGL

Translation of the website [https://learnopengl.com/](https://learnopengl.com/) to pt-br

[website link](https://filipecn.github.io/aprendaopengl/)

# translate.py
There is a little tool that you can use to help you translate to your own language as well. The script `translate.py` (located in the root folder of this repository) uses google translate service to generate a markdown file with all the translated content from a post from the original website. 

The script is crafted to handle the [https://learnopengl.com/](https://learnopengl.com/) posts, but should be straightforward to adapt it to your needs. **Always remember to review the google translated output because it comes with LOTS of errors, it is far from perfect!**

The usage of the script is very simple (you can use --help to check usage). The required command arguments are:

1 - url of the page you want to translate
2 - translated output markdown file location

Optional arguments to adjust to your language are:
--output_language: language to be translated to, default='pt'
--google_translate_link: link to google translate service, default='translate.google.com.br'
--verbose: print translation progress

Example:
``` shell
 python3 translate.py https://learnopengl.com/Lighting/Materials content/iluminacao/materiais/_index.md
```
