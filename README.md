## Earthly commands

- brew install earthly/earthly/earthly && earthly bootstrap
- earthly --allow-privileged +docker
- docker run --rm cmake-test:latest
- podman run --rm cmake-test:latest
- earthly +docker --tag='my-new-image-tag'
- earthly -i -P +generate-phrase
- earthly --build-arg NO_CACHE=true +generate-phrase
- earthly --no-cache +generate-phrase

## Task commands

- Reading a Taskfile from stdin

```bash
task -t - <(cat ./Taskfile.yml)
# OR
cat ./Taskfile.yml | task -t -
```

- task -a
- task --parallel task-to-be-called another-task
- [Usage](https://taskfile.dev/usage)

## References

- Using Docker with Earthly: [link 1](https://github.com/earthly/earthly/blob/main/examples/tutorial/js/part6/Earthfile) and [link 2](https://docs.earthly.dev/basics/part-6-using-docker-with-earthly)
- [Debugging techniques](https://docs.earthly.dev/docs/guides/debugging) and [Usage](https://taskfile.dev/usage)
- [Best practices](https://docs.earthly.dev/docs/guides/best-practices)
- [monorepo example](https://github.dev/furqanshahid85-python/python-monerepo/blob/main/earthly/requirements.txt)
- [Rust functions](https://github.com/earthly/lib/blob/main/rust/README.md)
- [Google OAuth 2.0 Playground](https://developers.google.com/oauthplayground)
- [Google OAuth 2.0 Scopes](https://developers.google.com/identity/protocols/oauth2/scopes)
- [Using OAuth 2.0 for Web Server Applications](https://developers.google.com/identity/protocols/oauth2/web-server)
- [How to get Access token](https://www.daimto.com/how-to-get-a-google-access-token-with-curl)
