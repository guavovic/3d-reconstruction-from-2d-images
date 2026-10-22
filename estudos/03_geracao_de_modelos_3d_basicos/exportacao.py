import os
import trimesh
import estudos.utils as utils

def exportar_malha(malha, tipo_malha, output_directory):
    
    filename = utils.get_unique_filename(output_directory, tipo_malha + '.obj') 
    save_path = os.path.join(output_directory, filename)
    
    malha.export(save_path)
    print('Malha gerada e salva em ' + save_path)
    
    mesh = trimesh.load(save_path)
    print('\n' + str(mesh.vertices_))