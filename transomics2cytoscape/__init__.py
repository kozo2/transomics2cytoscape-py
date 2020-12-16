import pandas as pd
import py4cytoscape as p4c
from Bio.KEGG.REST import kegg_get

def create3Dnetwork(networkLayers):
    layerTable = pd.read_csv(networkLayers, sep="\t", header=None)
    networkSUIDs = []
    zheightFor = {}
    for i, row in layerTable.iterrows():
        pathwayID = row[1]
        zheight = row[2]
        kgml = kegg_get(pathwayID, option="kgml").read()
        filename = pathwayID + '.xml'
        f = open(filename, 'w')
        f.write(kgml)
        f.close()
        res = p4c.import_network_from_file(file=filename)
        suid = res['networks'][0]
        networkSUIDs.append(suid)
        zheightFor[suid] = zheight
    
    nodetables = []
    for suid in networkSUIDs:
        nt = p4c.get_table_columns(table = "node", network = suid)
        nt['KEGG_NODE_Z'] = zheightFor[suid]
        nodetables.append(nt)
    layeredNodes = pd.concat(nodetables).rename(columns={"SUID": "id"})
#    return layeredNodes

    edgetables = []
    for suid in zheightFor:
        et = p4c.get_table_columns(table = "edge", network = suid)
        ei = p4c.get_edge_info(et['SUID'].tolist(), network = suid)
        edgetables.append(pd.DataFrame.from_dict(ei))
    layeredEdges = pd.concat(edgetables)

    p4c.commands_post('cy3d set renderer')
    layeredNodes = layeredNodes.applymap(str)
    layeredEdges = layeredEdges.applymap(str)
    suid = p4c.create_network_from_data_frames(layeredNodes, layeredEdges)
    # p4c.set_transomic_style(stylexml, suid)
    # return suid

def importLayer2(row):
    """
    docstring

    Parameters
    ----------

    Returns
    -------

    Examples
    --------
    """
    
    pass

def createTransomicsEdge(parameter_list):
    """
    docstring

    Parameters
    ----------

    Returns
    -------

    Examples
    --------
    """
    pass