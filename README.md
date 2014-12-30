Work in progress, dockerifying [abesto.net](http://abesto.net). Start the whole site with `run.sh`, try it like `curl $(boot2docker ip) -H 'Host: abesto.net'`. Then stop it with `stop.sh`.

Add this line to your hosts file to see it in "production":

```
212.71.254.167 abesto.net board.abesto.net
```

What's included so far:

 * HAProxy (routes by `Host` header)
  * [blog](https://github.com/abesto/blog) (host `abesto.net`)
  * [are-you-board](https://github.com/abesto/are-you-board) (host `board.abesto.net`)
   * A standalone Redis container serving as the database for `are-you-board`
