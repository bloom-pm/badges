import os
import SVGCompress

def compress_all_svgs(directory, compression_type, curve_fidelity=10, pre_select=False, selection_tuple=('', ''), optimize=True, **kwargs):
    for filename in os.listdir(directory):
        if filename.endswith(".svg"):
            full_path = os.path.join(directory, filename)
            output_file = full_path.replace('.svg', '_compressed.svg')  # Modify as needed
            SVGCompress.compress_by_method(
                filename=full_path, 
                compression_type=compression_type, 
                curve_fidelity=curve_fidelity, 
                outputfile=output_file, 
                pre_select=pre_select, 
                selection_tuple=selection_tuple, 
                optimize=optimize, 
                **kwargs
            )

if __name__ == "__main__":
    # Example usage, compressing with 'merge' method
    compress_all_svgs(
        directory='.',
        compression_type='merge',
        curve_fidelity=10,
        pre_select=True,
        selection_tuple=('bboxarea', 300),
        optimize=True,
        epsilon=5,
        bufferDistance=5,
        operation_key='hull'
    )

