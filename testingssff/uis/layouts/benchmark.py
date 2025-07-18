import gradio

from testingssff import state_manager
from testingssff.download import conditional_download, resolve_download_url
from testingssff.uis.components import about, age_modifier_options, benchmark, benchmark_options, deep_swapper_options, download, execution, execution_queue_count, execution_thread_count, expression_restorer_options, face_debugger_options, face_editor_options, face_enhancer_options, face_swapper_options, frame_colorizer_options, frame_enhancer_options, lip_syncer_options, memory, processors


def pre_check() -> bool:
	conditional_download('.assets/examples',
	[
		resolve_download_url('examples-3.0.0', 'source.jpg'),
		resolve_download_url('examples-3.0.0', 'source.mp3'),
		resolve_download_url('examples-3.0.0', 'target-240p.mp4'),
		resolve_download_url('examples-3.0.0', 'target-360p.mp4'),
		resolve_download_url('examples-3.0.0', 'target-540p.mp4'),
		resolve_download_url('examples-3.0.0', 'target-720p.mp4'),
		resolve_download_url('examples-3.0.0', 'target-1080p.mp4'),
		resolve_download_url('examples-3.0.0', 'target-1440p.mp4'),
		resolve_download_url('examples-3.0.0', 'target-2160p.mp4')
	])
	return True


def render() -> gradio.Blocks:
	with gradio.Blocks() as layout:
		with gradio.Row():
			with gradio.Column(scale = 4):
				with gradio.Blocks():
					about.render()
				with gradio.Blocks():
					processors.render()
				with gradio.Blocks():
					age_modifier_options.render()
				with gradio.Blocks():
					deep_swapper_options.render()
				with gradio.Blocks():
					expression_restorer_options.render()
				with gradio.Blocks():
					face_debugger_options.render()
				with gradio.Blocks():
					face_editor_options.render()
				with gradio.Blocks():
					face_enhancer_options.render()
				with gradio.Blocks():
					face_swapper_options.render()
				with gradio.Blocks():
					frame_colorizer_options.render()
				with gradio.Blocks():
					frame_enhancer_options.render()
				with gradio.Blocks():
					lip_syncer_options.render()
				with gradio.Blocks():
					execution.render()
					execution_thread_count.render()
					execution_queue_count.render()
				with gradio.Blocks():
					download.render()
				with gradio.Blocks():
					state_manager.set_item('video_memory_strategy', 'tolerant')
					memory.render()
				with gradio.Blocks():
					benchmark_options.render()
			with gradio.Column(scale = 11):
				with gradio.Blocks():
					benchmark.render()
	return layout


def listen() -> None:
	processors.listen()
	age_modifier_options.listen()
	deep_swapper_options.listen()
	expression_restorer_options.listen()
	download.listen()
	face_debugger_options.listen()
	face_editor_options.listen()
	face_enhancer_options.listen()
	face_swapper_options.listen()
	frame_colorizer_options.listen()
	frame_enhancer_options.listen()
	lip_syncer_options.listen()
	execution.listen()
	execution_thread_count.listen()
	execution_queue_count.listen()
	memory.listen()
	benchmark.listen()


def run(ui : gradio.Blocks) -> None:
	ui.launch(favicon_path = 'testingssff.ico', inbrowser = state_manager.get_item('open_browser'))
