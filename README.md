# IDE_on_Colab

[Google Colab](https://colab.research.google.com/) is a cloud-based platform that allows users to write, run, and share code in an interactive environment. It provides free access to computing resources, including GPU and TPU accelerators, to execute machine learning models and data analysis tasks. Colab is built on top of Jupyter notebooks and supports a variety of programming languages, including Python and R. Users can collaborate with others in real-time, import and export notebooks, and store their work on Google Drive. Overall, Google Colab is a powerful tool for data scientists, researchers, and educators to experiment and prototype their ideas.

As a cloud computing platform based on Jupyter notebooks, Google Colab does not provide a top-notch comfortable environment for R language data analysis and other non-Python programming. Therefore, this project provides a method for quickly installing other web IDE on Google Colab, enabling it to expand its range of capabilities.

## Usage

To get started, open the notebook [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/yimingsun12138/IDE_on_Colab/blob/main/Web_IDE_on_Colab.ipynb) and select the web IDE that you prefer. Once you have made your selection, complete the global setting and let me take care of the rest. If you opt for using the built-in tunnelling methods, upon completion of the process, a URL will be provided that can be used to access your web IDE.

You can also use the notebooks with more features provided for each web IDE in the section below.

## Web IDE supported

### Rstudio server

[Rstudio server](https://posit.co/) is a web IDE for R programming. With Rstudio server, users can run R scripts, create and manage R projects, develop and test code, and share their work with others. Rstudio server also offers powerful features such as syntax highlighting, code completion, debugging and data visualization.

### code server

[code server](https://github.com/coder/code-server) is a web IDE provided by [Coder](https://coder.com/) that enables developers to write, run and debug code from a web browser. It is built on the open-source Visual Studio Code editor and offers many of the same features, such as code highlighting, auto completion, and debugging.

## Port forwarding

This project integrates [localtunnel](https://github.com/localtunnel/localtunnel) and [ngrok](https://ngrok.com/) for internal network penetration, but you can always choose to use your own tunnelling methods.

Currently, an error ("WebSocket close with status code 1006") occurs when using localtunnel to proxy code server. I am not sure how to solve this problem at the moment, so I would recommend using ngrok instead. Sign up your own ngrok account, it also provides free service as localtunnel!
