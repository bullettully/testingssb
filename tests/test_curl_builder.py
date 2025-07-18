from shutil import which

from testingssff import metadata
from testingssff.curl_builder import chain, head, run


def test_run() -> None:
	user_agent = metadata.get('name') + '/' + metadata.get('version')

	assert run([]) == [ which('curl'), '--user-agent', user_agent, '--insecure', '--location', '--silent' ]


def test_chain() -> None:
	assert chain(head(metadata.get('url'))) == [ '-I', metadata.get('url') ]
