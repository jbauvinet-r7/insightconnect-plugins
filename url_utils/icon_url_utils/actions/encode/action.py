import insightconnect_plugin_runtime
from .schema import EncodeInput, EncodeOutput, Input, Output, Component
from urllib.parse import quote


class Encode(insightconnect_plugin_runtime.Action):
    def __init__(self):
        super(self.__class__, self).__init__(
            name="encode",
            description=Component.DESCRIPTION,
            input=EncodeInput(),
            output=EncodeOutput(),
        )

    def run(self, params={}):
        input_url = params.get(Input.URL)
        encode_all = params.get(Input.encode_all)

        url = input_url.split('://', maxsplit=1)

        if encode_all:
            url[-1] = quote(url[-1], safe='')
        else:
            url[-1] = quote(url[-1], safe='/?=&')

        result = '://'.join(url)

        return {Output.URL: result}