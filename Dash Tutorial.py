{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 2,
   "id": "12b24c01",
   "metadata": {},
   "outputs": [],
   "source": [
    "import dash\n",
    "import dash_core_components as dcc\n",
    "import dash_html_components as html"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 4,
   "id": "11e5133f",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Dash is running on http://127.0.0.1:8050/\n",
      "\n",
      "Dash is running on http://127.0.0.1:8050/\n",
      "\n",
      " * Serving Flask app \"__main__\" (lazy loading)\n",
      " * Environment: production\n",
      "\u001b[31m   WARNING: This is a development server. Do not use it in a production deployment.\u001b[0m\n",
      "\u001b[2m   Use a production WSGI server instead.\u001b[0m\n",
      " * Debug mode: on\n"
     ]
    },
    {
     "ename": "OSError",
     "evalue": "[Errno 48] Address already in use",
     "output_type": "error",
     "traceback": [
      "\u001b[0;31m---------------------------------------------------------------------------\u001b[0m",
      "\u001b[0;31mOSError\u001b[0m                                   Traceback (most recent call last)",
      "\u001b[0;32m<ipython-input-4-b5e49bb86fd2>\u001b[0m in \u001b[0;36m<module>\u001b[0;34m\u001b[0m\n\u001b[1;32m      4\u001b[0m \u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m      5\u001b[0m \u001b[0;32mif\u001b[0m \u001b[0m__name__\u001b[0m \u001b[0;34m==\u001b[0m \u001b[0;34m'__main__'\u001b[0m\u001b[0;34m:\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0;32m----> 6\u001b[0;31m     \u001b[0mapp\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0mrun_server\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0mdebug\u001b[0m\u001b[0;34m=\u001b[0m\u001b[0;32mTrue\u001b[0m\u001b[0;34m,\u001b[0m\u001b[0mhost\u001b[0m \u001b[0;34m=\u001b[0m \u001b[0;34m'127.0.0.1'\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0m\u001b[1;32m      7\u001b[0m \u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m      8\u001b[0m \u001b[0;34m\u001b[0m\u001b[0m\n",
      "\u001b[0;32m~/.local/lib/python3.8/site-packages/dash/dash.py\u001b[0m in \u001b[0;36mrun_server\u001b[0;34m(self, host, port, proxy, debug, dev_tools_ui, dev_tools_props_check, dev_tools_serve_dev_bundles, dev_tools_hot_reload, dev_tools_hot_reload_interval, dev_tools_hot_reload_watch_interval, dev_tools_hot_reload_max_retry, dev_tools_silence_routes_logging, dev_tools_prune_errors, **flask_run_options)\u001b[0m\n\u001b[1;32m   2031\u001b[0m                     \u001b[0mextra_files\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0mappend\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0mpath\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m   2032\u001b[0m \u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0;32m-> 2033\u001b[0;31m         \u001b[0mself\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0mserver\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0mrun\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0mhost\u001b[0m\u001b[0;34m=\u001b[0m\u001b[0mhost\u001b[0m\u001b[0;34m,\u001b[0m \u001b[0mport\u001b[0m\u001b[0;34m=\u001b[0m\u001b[0mport\u001b[0m\u001b[0;34m,\u001b[0m \u001b[0mdebug\u001b[0m\u001b[0;34m=\u001b[0m\u001b[0mdebug\u001b[0m\u001b[0;34m,\u001b[0m \u001b[0;34m**\u001b[0m\u001b[0mflask_run_options\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0m",
      "\u001b[0;32m/opt/anaconda3/lib/python3.8/site-packages/flask/app.py\u001b[0m in \u001b[0;36mrun\u001b[0;34m(self, host, port, debug, load_dotenv, **options)\u001b[0m\n\u001b[1;32m    988\u001b[0m \u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m    989\u001b[0m         \u001b[0;32mtry\u001b[0m\u001b[0;34m:\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0;32m--> 990\u001b[0;31m             \u001b[0mrun_simple\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0mhost\u001b[0m\u001b[0;34m,\u001b[0m \u001b[0mport\u001b[0m\u001b[0;34m,\u001b[0m \u001b[0mself\u001b[0m\u001b[0;34m,\u001b[0m \u001b[0;34m**\u001b[0m\u001b[0moptions\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0m\u001b[1;32m    991\u001b[0m         \u001b[0;32mfinally\u001b[0m\u001b[0;34m:\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m    992\u001b[0m             \u001b[0;31m# reset the first request information if the development server\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n",
      "\u001b[0;32m/opt/anaconda3/lib/python3.8/site-packages/werkzeug/serving.py\u001b[0m in \u001b[0;36mrun_simple\u001b[0;34m(hostname, port, application, use_reloader, use_debugger, use_evalex, extra_files, reloader_interval, reloader_type, threaded, processes, request_handler, static_files, passthrough_errors, ssl_context)\u001b[0m\n\u001b[1;32m   1028\u001b[0m             \u001b[0ms\u001b[0m \u001b[0;34m=\u001b[0m \u001b[0msocket\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0msocket\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0maddress_family\u001b[0m\u001b[0;34m,\u001b[0m \u001b[0msocket\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0mSOCK_STREAM\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m   1029\u001b[0m             \u001b[0ms\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0msetsockopt\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0msocket\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0mSOL_SOCKET\u001b[0m\u001b[0;34m,\u001b[0m \u001b[0msocket\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0mSO_REUSEADDR\u001b[0m\u001b[0;34m,\u001b[0m \u001b[0;36m1\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0;32m-> 1030\u001b[0;31m             \u001b[0ms\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0mbind\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0mserver_address\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0m\u001b[1;32m   1031\u001b[0m             \u001b[0;32mif\u001b[0m \u001b[0mhasattr\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0ms\u001b[0m\u001b[0;34m,\u001b[0m \u001b[0;34m\"set_inheritable\"\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m:\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m   1032\u001b[0m                 \u001b[0ms\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0mset_inheritable\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0;32mTrue\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n",
      "\u001b[0;31mOSError\u001b[0m: [Errno 48] Address already in use"
     ]
    }
   ],
   "source": [
    "app = dash.Dash()\n",
    "\n",
    "app.layout = html.Div(children=[html.H1(\"Dash_tutorials\")])\n",
    "\n",
    "if __name__ == '__main__':\n",
    "    app.run_server(debug=True,host = '127.0.0.1')\n",
    "\n",
    "\n",
    "\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 4,
   "id": "d955c6d7",
   "metadata": {},
   "outputs": [
    {
     "ename": "NameError",
     "evalue": "name 'Dash' is not defined",
     "output_type": "error",
     "traceback": [
      "\u001b[0;31m---------------------------------------------------------------------------\u001b[0m",
      "\u001b[0;31mNameError\u001b[0m                                 Traceback (most recent call last)",
      "\u001b[0;32m<ipython-input-4-b8736dd8273b>\u001b[0m in \u001b[0;36m<module>\u001b[0;34m\u001b[0m\n\u001b[1;32m      8\u001b[0m \u001b[0;32mimport\u001b[0m \u001b[0mpandas\u001b[0m \u001b[0;32mas\u001b[0m \u001b[0mpd\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m      9\u001b[0m \u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0;32m---> 10\u001b[0;31m \u001b[0mapp\u001b[0m \u001b[0;34m=\u001b[0m \u001b[0mDash\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0m__name__\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0m\u001b[1;32m     11\u001b[0m \u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m     12\u001b[0m \u001b[0;31m# assume you have a \"long-form\" data frame\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n",
      "\u001b[0;31mNameError\u001b[0m: name 'Dash' is not defined"
     ]
    }
   ],
   "source": [
    "# Run this app with `python app.py` and\n",
    "# visit http://127.0.0.1:8050/ in your web browser.\n",
    "\n",
    "\n",
    "app = Dash(__name__)\n",
    "\n",
    "# assume you have a \"long-form\" data frame\n",
    "# see https://plotly.com/python/px-arguments/ for more options\n",
    "df = pd.DataFrame({\n",
    "    \"Fruit\": [\"Apples\", \"Oranges\", \"Bananas\", \"Apples\", \"Oranges\", \"Bananas\"],\n",
    "    \"Amount\": [4, 1, 2, 2, 4, 5],\n",
    "    \"City\": [\"SF\", \"SF\", \"SF\", \"Montreal\", \"Montreal\", \"Montreal\"]\n",
    "})\n",
    "\n",
    "fig = px.bar(df, x=\"Fruit\", y=\"Amount\", color=\"City\", barmode=\"group\")\n",
    "\n",
    "app.layout = html.Div(children=[\n",
    "    html.H1(children='Hello Dash'),\n",
    "\n",
    "    html.Div(children='''\n",
    "        Dash: A web application framework for your data.\n",
    "    '''),\n",
    "\n",
    "    dcc.Graph(\n",
    "        id='example-graph',\n",
    "        figure=fig\n",
    "    )\n",
    "])\n",
    "\n",
    "if __name__ == '__main__':\n",
    "    app.run_server(debug=True)\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "df600710",
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3",
   "language": "python",
   "name": "python3"
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
   "version": "3.8.8"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
