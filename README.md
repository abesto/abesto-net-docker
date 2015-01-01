Work in progress, dockerifying [abesto.net](http://abesto.net).

Requirements:
 - [Docker](https://www.docker.com/)
 - [fig](http://www.fig.sh/)

## Running locally
```sh
. ./dev.env # Load env variables for volume mount points for running locally (there's also prod.env)
fig pull    # Pull the latest version of all relevant docker repos. Also do this to update versions.
fug up -d   # Start the whole shebang
curl $(boot2docker ip) -H 'Host: abesto.net'  # Look at the blog; use 127.0.0.1 if on Linux and not using boot2docker
fig stop    # Stop and delete containers
```

## In production

Add this line to your hosts file to see it in "production":

```
212.71.254.167 abesto.net board.abesto.net mastermind.abesto.net algo.abesto.net
```

## What's included so far

A requst travels down this path:

 * HAProxy (routes by `Host` header)
  * [blog](https://github.com/abesto/blog) (host [abesto.net](http://abesto.net))
  * [are-you-board](https://github.com/abesto/are-you-board) (host [board.abesto.net](http://board.abesto.net))
    * A standalone Redis container serving as the database for `are-you-board`
  * [mastermind](https://github.com/abesto/mastermind) (host [mastermind.abesto.net](http://mastermind.abesto.net))
  * [algo](https://github.com/abesto/algo) (host [algo.abesto.net](http://algo.abesto.net))
