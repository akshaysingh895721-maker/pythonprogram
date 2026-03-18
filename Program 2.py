{
  "nbformat": 4,
  "nbformat_minor": 0,
  "metadata": {
    "colab": {
      "provenance": [],
      "authorship_tag": "ABX9TyPCYPuu7gl8QwbOHFP2xyfj",
      "include_colab_link": true
    },
    "kernelspec": {
      "name": "python3",
      "display_name": "Python 3"
    },
    "language_info": {
      "name": "python"
    }
  },
  "cells": [
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "view-in-github",
        "colab_type": "text"
      },
      "source": [
        "<a href=\"https://colab.research.google.com/github/akshaysingh895721-maker/pythonprogram/blob/main/Program%202.py\" target=\"_parent\"><img src=\"https://colab.research.google.com/assets/colab-badge.svg\" alt=\"Open In Colab\"/></a>"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": 1,
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "IjL8pA5gIZ-g",
        "outputId": "c16d3f89-2dce-4190-8583-697ac3ba03fa"
      },
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "Enter age: 19\n",
            "Eligible\n"
          ]
        }
      ],
      "source": [
        "#program to check eligible for vote or Not\n",
        "\n",
        "# Take input from user\n",
        "age = int(input(\"Enter age: \"))\n",
        "\n",
        "# Checking eligibility\n",
        "if age >= 18:\n",
        "    print(\"Eligible\")\n",
        "else:\n",
        "    print(\"Not Eligible\")"
      ]
    }
  ]
}