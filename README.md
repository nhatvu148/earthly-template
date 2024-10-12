## Earthly commands

- brew install earthly/earthly/earthly && earthly bootstrap
- earthly --allow-privileged +docker
- docker run --rm cmake-test:latest
- podman run --rm cmake-test:latest
- earthly +docker --tag='my-new-image-tag'
- earthly -i -P +generate-phrase
- earthly --build-arg NO_CACHE=true +generate-phrase
- earthly --no-cache +generate-phrase

## References

- Using Docker with Earthly: [link 1](https://github.com/earthly/earthly/blob/main/examples/tutorial/js/part6/Earthfile) and [link 2](https://docs.earthly.dev/basics/part-6-using-docker-with-earthly)
- [Debugging techniques](https://docs.earthly.dev/docs/guides/debugging)
- [Best practices](https://docs.earthly.dev/docs/guides/best-practices)
- [monorepo example](https://github.dev/furqanshahid85-python/python-monerepo/blob/main/earthly/requirements.txt)
- [Rust functions](https://github.com/earthly/lib/blob/main/rust/README.md)
