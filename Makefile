SPEC_URL := https://kagi.redocly.app/_spec/openapi.yaml

generate:
	openapi-generator-cli generate \
		-i $(SPEC_URL) \
		-g python \
		-o . \
		-c config.yaml \
		-t templates/
