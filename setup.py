{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 1,
   "id": "242423e0-f719-4ed3-b7ab-b315a1e70e08",
   "metadata": {},
   "outputs": [
    {
     "ename": "SystemExit",
     "evalue": "usage: ipykernel_launcher.py [global_opts] cmd1 [cmd1_opts] [cmd2 [cmd2_opts] ...]\n   or: ipykernel_launcher.py --help [cmd1 cmd2 ...]\n   or: ipykernel_launcher.py --help-commands\n   or: ipykernel_launcher.py cmd --help\n\nerror: option -f not recognized",
     "output_type": "error",
     "traceback": [
      "An exception has occurred, use %tb to see the full traceback.\n",
      "\u001b[1;31mSystemExit\u001b[0m\u001b[1;31m:\u001b[0m usage: ipykernel_launcher.py [global_opts] cmd1 [cmd1_opts] [cmd2 [cmd2_opts] ...]\n   or: ipykernel_launcher.py --help [cmd1 cmd2 ...]\n   or: ipykernel_launcher.py --help-commands\n   or: ipykernel_launcher.py cmd --help\n\nerror: option -f not recognized\n"
     ]
    },
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "C:\\Users\\mateu\\anaconda3\\Lib\\site-packages\\IPython\\core\\interactiveshell.py:3585: UserWarning: To exit: use 'exit', 'quit', or Ctrl-D.\n",
      "  warn(\"To exit: use 'exit', 'quit', or Ctrl-D.\", stacklevel=1)\n"
     ]
    }
   ],
   "source": [
    "from setuptools import setup, find_packages\n",
    "\n",
    "setup(\n",
    "    name='statspy',\n",
    "    version='0.1.0',\n",
    "    description='A simple example Python library',\n",
    "    author='Mateus Augusto da Silva Ali Fontes',\n",
    "    packages=find_packages(),\n",
    "    install_requires=[],  # List dependencies here\n",
    ")"
   ]
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python [conda env:base] *",
   "language": "python",
   "name": "conda-base-py"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.12.7"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
