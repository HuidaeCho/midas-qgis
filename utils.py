import tempfile
import os
import subprocess

from qgis.core import (QgsRasterFileWriter,
                       QgsVectorFileWriter,
                       QgsProcessingException)

def export_raster_to_tempfile(raster_layer, context):
    temp_file = tempfile.NamedTemporaryFile(suffix=".tif", delete=False)
    temp_path = temp_file.name
    temp_file.close()

    writer = QgsRasterFileWriter(temp_path)
    pipe = QgsRasterPipe()
    pipe.set(raster_layer.dataProvider().clone())

    error = writer.writeRaster(
        pipe,
        raster_layer.width(),
        raster_layer.height(),
        raster_layer.extent(),
        raster_layer.crs(),
        context.transformContext()
    )

    if error != QgsRasterFileWriter.NoError:
        os.remove(temp_path)
        raise RuntimeError(f"Failed to write GeoTIFF: error code {error}")

    return temp_path

def export_vector_to_tempfile(vector_layer, context):
    temp_file = tempfile.NamedTemporaryFile(suffix=".gpkg", delete=False)
    temp_path = temp_file.name
    temp_file.close()

    options = QgsVectorFileWriter.SaveVectorOptions()
    options.driverName = "GPKG"
    options.fileEncoding = "UTF-8"
    options.layerName = "temp"

    error = QgsVectorFileWriter.writeAsVectorFormatV3(
        vector_layer,
        temp_path,
        context.transformContext(),
        options
    )

    if error != QgsVectorFileWriter.NoError:
        os.remove(temp_path)
        raise RuntimeError(f"Failed to write GeoPackage: error code {error}")

    return temp_path


def run_command_stream_output(cmd, feedback):
    with subprocess.Popen(
        cmd,
        stdout=subprocess.PIPE,
        stderr=subprocess.STDOUT,
        text=True,
        bufsize=1,
        universal_newlines=True
    ) as process:
        if process.stdout is not None:
            for line in process.stdout:
                feedback.pushConsoleInfo(line.strip())

        process.wait()
        if process.returncode != 0:
            raise QgsProcessingException(f"Process exited with code {process.returncode}")
