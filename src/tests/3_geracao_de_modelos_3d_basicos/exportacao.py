import os
import trimesh
import file_utils as fu

writePath = 'results/passo_3 (geração de modelos 3D básicos)/objs/'

def exportar_malha(malha, tipo_malha):
    
    filename = fu.get_unique_filename(writePath, tipo_malha + '.obj') 
    save_path = os.path.join(writePath, filename)
    
    malha.export(save_path)
    print('Malha gerada e salva em ' + save_path)
    
    mesh = trimesh.load(save_path)
    print('\n' + str(mesh.vertices_))