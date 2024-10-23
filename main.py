import apache_beam as beam
from apache_beam.options.pipeline_options import PipelineOptions, GoogleCloudOptions, StandardOptions

class SimpleTransform(beam.DoFn):
    def process(self, element):
        # Example transformation: Convert text to uppercase
        return [element.upper()]

def run(argv=None):
    # Define pipeline options
    pipeline_options = PipelineOptions(argv)
    google_cloud_options = pipeline_options.view_as(GoogleCloudOptions)

    google_cloud_options.project = 'nasir-438710'
    google_cloud_options.region = 'asia-southeast1'  # e.g., 'us-central1'
    google_cloud_options.staging_location = 'gs://cloud7-dataflow-templates/staging'
    google_cloud_options.temp_location = 'gs://cloud7-dataflow-templates/temp'
    google_cloud_options.template_location = 'gs://cloud7-dataflow-templates/templates/python_template_1'

    pipeline_options.view_as(StandardOptions).runner = 'DataflowRunner'

    # Create a pipeline
    with beam.Pipeline(options=pipeline_options) as p:
        (
            p
            | 'ReadFromText' >> beam.io.ReadFromText('gs://cloud7-dataflow-templates/input.txt')
            | 'TransformText' >> beam.ParDo(SimpleTransform())
            | 'WriteToText' >> beam.io.WriteToText('gs://cloud7-dataflow-templates/output')
        )

if __name__ == '__main__':
    run()