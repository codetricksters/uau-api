# ContratoMaterialServico

## POST `/api/ContratoMaterialServico/obterListaEstruturaAprovacoes`

### Parâmetros

| Nome | Em | Tipo | Obrigatório | Descrição |
|---|---|---|---|---|
| `intNumAprov` | query | integer (int32) | ✓ |  |
| `tipoAprovacao` | query | integer (int32) | ✓ |  |
| `tipoPedido` | query | integer (int32) — valores possíveis: 0, 1, 2 |  |  |
| `api-version` | query | string |  |  |
| `gerAprov._listaEstruturaDeAprovacao` | query | array de object |  |  |
| `gerAprov.codigoDaEmpresa` | query | integer (int32) |  |  |
| `gerAprov.codigoDaObra` | query | string |  |  |
| `gerAprov.tipoDoProcesso` | query | integer (int32) |  |  |
| `gerAprov.quantidadeAprovacao` | query | integer (int32) |  |  |
| `gerAprov.valorSolicitado` | query | number (double) |  |  |
| `gerAprov.usuarioLogado` | query | string |  |  |
| `gerAprov.acao` | query | integer (int32) — valores possíveis: 0, 1, 3 |  |  |
| `gerAprov.estruturaAprovacao` | query | integer (int32) |  |  |
| `gerAprov.estruturaAprovFaixaValor` | query | integer (int32) |  |  |
| `gerAprov.codigoDepartamento` | query | string |  |  |
| `gerAprov.codigoCargo` | query | string |  |  |
| `gerAprov.listaSeqPendAprovAbaixoSeqUsuarioLog` | query | array de object |  |  |
| `gerAprov.isAprovForaSequencia` | query | boolean |  |  |
| `gerAprov.chaveJustificativaAprovacao` | query | string |  |  |
| `repAprovSimulaConf.stringFormat` | query | string |  |  |
| `repAprovSimulaConf.empresa_apSC` | query | integer (int32) |  |  |
| `repAprovSimulaConf.obra_apSC` | query | string |  |  |
| `repAprovSimulaConf.numeroSim_apSC` | query | integer (int32) |  |  |
| `repAprovSimulaConf.numCot_apSC` | query | integer (int32) |  |  |
| `repAprovSimulaConf.usrAprov_apSC` | query | string |  |  |
| `repAprovSimulaConf.dataAprov_apSC` | query | string (date-time) |  |  |
| `repAprovSimulaConf.codCargo_ApSC` | query | string |  |  |
| `repAprovSimulaConf.codDep_ApSC` | query | string |  |  |
| `repAprovSimulaConf.numJusAprov_apSC` | query | integer (int32) |  |  |
| `repAprovSimulaConf.num_apSC` | query | integer (int32) |  |  |
| `repAprovSimulaConf.s_Empresa_apSC` | query | string |  |  |
| `repAprovSimulaConf.s_Obra_apSC` | query | string |  |  |
| `repAprovSimulaConf.s_NumeroSim_apSC` | query | string |  |  |
| `repAprovSimulaConf.s_NumCot_apSC` | query | string |  |  |
| `repAprovSimulaConf.s_UsrAprov_apSC` | query | string |  |  |
| `repAprovSimulaConf.s_DataAprov_apSC` | query | string |  |  |
| `repAprovSimulaConf.s_CodCargo_ApSC` | query | string |  |  |
| `repAprovSimulaConf.s_CodDep_ApSC` | query | string |  |  |
| `repAprovSimulaConf.s_NumJusAprov_apSC` | query | string |  |  |
| `repAprovSimulaConf.s_Num_apSC` | query | string |  |  |
| `repAprovSimulaConf.querySource` | query | string |  |  |
| `repAprovSimulaConf.mappingName` | query | string |  |  |
| `repAprovSimulaConf.schemaGlobal` | query | string |  |  |
| `repAprovSimulaConf.schemaTableView` | query | string |  |  |
| `repAprovSimulaConf.schemaStoredProcedure` | query | string |  |  |
| `repAprovSimulaConf.notRecommendedConnection.connectionString` | query | string |  |  |
| `repAprovSimulaConf.notRecommendedConnection.commandTimeout` | query | integer (int32) |  |  |
| `repAprovSimulaConf.notRecommendedConnection.connectionTimeout` | query | integer (int32) |  |  |
| `repAprovSimulaConf.notRecommendedConnection.defaultDatabase` | query | string |  |  |
| `repAprovSimulaConf.notRecommendedConnection.isolationLevel` | query | integer (int32) — valores possíveis: 16, 256, 256, 4096, 4096, 65536, 1048576, 1048576, -1 |  |  |
| `repAprovSimulaConf.notRecommendedConnection.attributes` | query | integer (int32) |  |  |
| `repAprovSimulaConf.notRecommendedConnection.cursorLocation` | query | integer (int32) — valores possíveis: 1, 2, 3, 3 |  |  |
| `repAprovSimulaConf.notRecommendedConnection.mode` | query | integer (int32) — valores possíveis: 0, 1, 2, 3, 4, 8, 12, 16, 4194304 |  |  |
| `repAprovSimulaConf.notRecommendedConnection.provider` | query | string |  |  |
| `repAprovSimulaConf.connectionString` | query | string |  |  |
| `repAprovSimulaConf.connectionStringConfig` | query | string |  |  |
| `repAprovSimulaConf.filter` | query | string |  |  |
| `repAprovSimulaConf.sort` | query | string |  |  |
| `repAprovCont.stringFormat` | query | string |  |  |
| `repAprovCont.empresa_ApCont` | query | integer (int32) |  |  |
| `repAprovCont.codCont_ApCont` | query | integer (int32) |  |  |
| `repAprovCont.usrAprov_ApCont` | query | string |  |  |
| `repAprovCont.dataAprov_ApCont` | query | string (date-time) |  |  |
| `repAprovCont.codCargo_ApCont` | query | string |  |  |
| `repAprovCont.codDep_ApCont` | query | string |  |  |
| `repAprovCont.numJusAprov_ApCont` | query | integer (int32) |  |  |
| `repAprovCont.num_ApCont` | query | integer (int32) |  |  |
| `repAprovCont.s_Empresa_ApCont` | query | string |  |  |
| `repAprovCont.s_CodCont_ApCont` | query | string |  |  |
| `repAprovCont.s_UsrAprov_ApCont` | query | string |  |  |
| `repAprovCont.s_DataAprov_ApCont` | query | string |  |  |
| `repAprovCont.s_CodCargo_ApCont` | query | string |  |  |
| `repAprovCont.s_CodDep_ApCont` | query | string |  |  |
| `repAprovCont.s_NumJusAprov_ApCont` | query | string |  |  |
| `repAprovCont.s_Num_ApCont` | query | string |  |  |
| `repAprovCont.querySource` | query | string |  |  |
| `repAprovCont.mappingName` | query | string |  |  |
| `repAprovCont.schemaGlobal` | query | string |  |  |
| `repAprovCont.schemaTableView` | query | string |  |  |
| `repAprovCont.schemaStoredProcedure` | query | string |  |  |
| `repAprovCont.notRecommendedConnection.connectionString` | query | string |  |  |
| `repAprovCont.notRecommendedConnection.commandTimeout` | query | integer (int32) |  |  |
| `repAprovCont.notRecommendedConnection.connectionTimeout` | query | integer (int32) |  |  |
| `repAprovCont.notRecommendedConnection.defaultDatabase` | query | string |  |  |
| `repAprovCont.notRecommendedConnection.isolationLevel` | query | integer (int32) — valores possíveis: 16, 256, 256, 4096, 4096, 65536, 1048576, 1048576, -1 |  |  |
| `repAprovCont.notRecommendedConnection.attributes` | query | integer (int32) |  |  |
| `repAprovCont.notRecommendedConnection.cursorLocation` | query | integer (int32) — valores possíveis: 1, 2, 3, 3 |  |  |
| `repAprovCont.notRecommendedConnection.mode` | query | integer (int32) — valores possíveis: 0, 1, 2, 3, 4, 8, 12, 16, 4194304 |  |  |
| `repAprovCont.notRecommendedConnection.provider` | query | string |  |  |
| `repAprovCont.connectionString` | query | string |  |  |
| `repAprovCont.connectionStringConfig` | query | string |  |  |
| `repAprovCont.filter` | query | string |  |  |
| `repAprovCont.sort` | query | string |  |  |
| `repAprovMed.stringFormat` | query | string |  |  |
| `repAprovMed.empresa_apmed` | query | integer (int32) |  |  |
| `repAprovMed.codCont_apmed` | query | integer (int32) |  |  |
| `repAprovMed.codMed_apmed` | query | integer (int32) |  |  |
| `repAprovMed.usrAprov_apmed` | query | string |  |  |
| `repAprovMed.dataAprov_apmed` | query | string (date-time) |  |  |
| `repAprovMed.codCargo_apmed` | query | string |  |  |
| `repAprovMed.codDep_apmed` | query | string |  |  |
| `repAprovMed.numJusAprov_apmed` | query | integer (int32) |  |  |
| `repAprovMed.num_apmed` | query | integer (int32) |  |  |
| `repAprovMed.s_Empresa_apmed` | query | string |  |  |
| `repAprovMed.s_CodCont_apmed` | query | string |  |  |
| `repAprovMed.s_CodMed_apmed` | query | string |  |  |
| `repAprovMed.s_UsrAprov_apmed` | query | string |  |  |
| `repAprovMed.s_DataAprov_apmed` | query | string |  |  |
| `repAprovMed.s_CodCargo_apmed` | query | string |  |  |
| `repAprovMed.s_CodDep_apmed` | query | string |  |  |
| `repAprovMed.s_NumJusAprov_apmed` | query | string |  |  |
| `repAprovMed.s_Num_apmed` | query | string |  |  |
| `repAprovMed.querySource` | query | string |  |  |
| `repAprovMed.mappingName` | query | string |  |  |
| `repAprovMed.schemaGlobal` | query | string |  |  |
| `repAprovMed.schemaTableView` | query | string |  |  |
| `repAprovMed.schemaStoredProcedure` | query | string |  |  |
| `repAprovMed.notRecommendedConnection.connectionString` | query | string |  |  |
| `repAprovMed.notRecommendedConnection.commandTimeout` | query | integer (int32) |  |  |
| `repAprovMed.notRecommendedConnection.connectionTimeout` | query | integer (int32) |  |  |
| `repAprovMed.notRecommendedConnection.defaultDatabase` | query | string |  |  |
| `repAprovMed.notRecommendedConnection.isolationLevel` | query | integer (int32) — valores possíveis: 16, 256, 256, 4096, 4096, 65536, 1048576, 1048576, -1 |  |  |
| `repAprovMed.notRecommendedConnection.attributes` | query | integer (int32) |  |  |
| `repAprovMed.notRecommendedConnection.cursorLocation` | query | integer (int32) — valores possíveis: 1, 2, 3, 3 |  |  |
| `repAprovMed.notRecommendedConnection.mode` | query | integer (int32) — valores possíveis: 0, 1, 2, 3, 4, 8, 12, 16, 4194304 |  |  |
| `repAprovMed.notRecommendedConnection.provider` | query | string |  |  |
| `repAprovMed.connectionString` | query | string |  |  |
| `repAprovMed.connectionStringConfig` | query | string |  |  |
| `repAprovMed.filter` | query | string |  |  |
| `repAprovMed.sort` | query | string |  |  |
| `repAprovSimula.stringFormat` | query | string |  |  |
| `repAprovSimula.empresa_apsim` | query | integer (int32) |  |  |
| `repAprovSimula.numSim_apsim` | query | integer (int32) |  |  |
| `repAprovSimula.numCot_apsim` | query | integer (int32) |  |  |
| `repAprovSimula.usrAprov_apsim` | query | string |  |  |
| `repAprovSimula.dataAprov_apsim` | query | string (date-time) |  |  |
| `repAprovSimula.codCargo_apsim` | query | string |  |  |
| `repAprovSimula.codDep_apsim` | query | string |  |  |
| `repAprovSimula.numJusAprov_apsim` | query | integer (int32) |  |  |
| `repAprovSimula.num_apsim` | query | integer (int32) |  |  |
| `repAprovSimula.s_Empresa_apsim` | query | string |  |  |
| `repAprovSimula.s_NumSim_apsim` | query | string |  |  |
| `repAprovSimula.s_NumCot_apsim` | query | string |  |  |
| `repAprovSimula.s_UsrAprov_apsim` | query | string |  |  |
| `repAprovSimula.s_DataAprov_apsim` | query | string |  |  |
| `repAprovSimula.s_CodCargo_apsim` | query | string |  |  |
| `repAprovSimula.s_CodDep_apsim` | query | string |  |  |
| `repAprovSimula.s_NumJusAprov_apsim` | query | string |  |  |
| `repAprovSimula.s_Num_apsim` | query | string |  |  |
| `repAprovSimula.querySource` | query | string |  |  |
| `repAprovSimula.mappingName` | query | string |  |  |
| `repAprovSimula.schemaGlobal` | query | string |  |  |
| `repAprovSimula.schemaTableView` | query | string |  |  |
| `repAprovSimula.schemaStoredProcedure` | query | string |  |  |
| `repAprovSimula.notRecommendedConnection.connectionString` | query | string |  |  |
| `repAprovSimula.notRecommendedConnection.commandTimeout` | query | integer (int32) |  |  |
| `repAprovSimula.notRecommendedConnection.connectionTimeout` | query | integer (int32) |  |  |
| `repAprovSimula.notRecommendedConnection.defaultDatabase` | query | string |  |  |
| `repAprovSimula.notRecommendedConnection.isolationLevel` | query | integer (int32) — valores possíveis: 16, 256, 256, 4096, 4096, 65536, 1048576, 1048576, -1 |  |  |
| `repAprovSimula.notRecommendedConnection.attributes` | query | integer (int32) |  |  |
| `repAprovSimula.notRecommendedConnection.cursorLocation` | query | integer (int32) — valores possíveis: 1, 2, 3, 3 |  |  |
| `repAprovSimula.notRecommendedConnection.mode` | query | integer (int32) — valores possíveis: 0, 1, 2, 3, 4, 8, 12, 16, 4194304 |  |  |
| `repAprovSimula.notRecommendedConnection.provider` | query | string |  |  |
| `repAprovSimula.connectionString` | query | string |  |  |
| `repAprovSimula.connectionStringConfig` | query | string |  |  |
| `repAprovSimula.filter` | query | string |  |  |
| `repAprovSimula.sort` | query | string |  |  |
| `rsAprovRequisicaoCompra.sort` | query | string |  |  |
| `repAprovacoesPL.stringFormat` | query | string |  |  |
| `repAprovacoesPL.numSap_ApPlan` | query | integer (int32) |  |  |
| `repAprovacoesPL.usrAprov_ApPlan` | query | string |  |  |
| `repAprovacoesPL.dataAprov_ApPlan` | query | string (date-time) |  |  |
| `repAprovacoesPL.codCargo_ApPlan` | query | string |  |  |
| `repAprovacoesPL.codDep_ApPlan` | query | string |  |  |
| `repAprovacoesPL.numJusAprov_ApPlan` | query | integer (int32) |  |  |
| `repAprovacoesPL.num_ApPlan` | query | integer (int32) |  |  |
| `repAprovacoesPL.s_NumSap_ApPlan` | query | string |  |  |
| `repAprovacoesPL.s_UsrAprov_ApPlan` | query | string |  |  |
| `repAprovacoesPL.s_DataAprov_ApPlan` | query | string |  |  |
| `repAprovacoesPL.s_CodCargo_ApPlan` | query | string |  |  |
| `repAprovacoesPL.s_CodDep_ApPlan` | query | string |  |  |
| `repAprovacoesPL.s_NumJusAprov_ApPlan` | query | string |  |  |
| `repAprovacoesPL.s_Num_ApPlan` | query | string |  |  |
| `repAprovacoesPL.querySource` | query | string |  |  |
| `repAprovacoesPL.mappingName` | query | string |  |  |
| `repAprovacoesPL.schemaGlobal` | query | string |  |  |
| `repAprovacoesPL.schemaTableView` | query | string |  |  |
| `repAprovacoesPL.schemaStoredProcedure` | query | string |  |  |
| `repAprovacoesPL.notRecommendedConnection.connectionString` | query | string |  |  |
| `repAprovacoesPL.notRecommendedConnection.commandTimeout` | query | integer (int32) |  |  |
| `repAprovacoesPL.notRecommendedConnection.connectionTimeout` | query | integer (int32) |  |  |
| `repAprovacoesPL.notRecommendedConnection.defaultDatabase` | query | string |  |  |
| `repAprovacoesPL.notRecommendedConnection.isolationLevel` | query | integer (int32) — valores possíveis: 16, 256, 256, 4096, 4096, 65536, 1048576, 1048576, -1 |  |  |
| `repAprovacoesPL.notRecommendedConnection.attributes` | query | integer (int32) |  |  |
| `repAprovacoesPL.notRecommendedConnection.cursorLocation` | query | integer (int32) — valores possíveis: 1, 2, 3, 3 |  |  |
| `repAprovacoesPL.notRecommendedConnection.mode` | query | integer (int32) — valores possíveis: 0, 1, 2, 3, 4, 8, 12, 16, 4194304 |  |  |
| `repAprovacoesPL.notRecommendedConnection.provider` | query | string |  |  |
| `repAprovacoesPL.connectionString` | query | string |  |  |
| `repAprovacoesPL.connectionStringConfig` | query | string |  |  |
| `repAprovacoesPL.filter` | query | string |  |  |
| `repAprovacoesPL.sort` | query | string |  |  |
| `repGerAprovacaoMat.stringFormat` | query | string |  |  |
| `repGerAprovacaoMat.empresa_ApPedM` | query | integer (int32) |  |  |
| `repGerAprovacaoMat.obra_ApPedM` | query | string |  |  |
| `repGerAprovacaoMat.insumo_ApPedM` | query | string |  |  |
| `repGerAprovacaoMat.numPedido_ApPedM` | query | integer (int32) |  |  |
| `repGerAprovacaoMat.itemPed_ApPedM` | query | integer (int32) |  |  |
| `repGerAprovacaoMat.usrAprov_ApPedM` | query | string |  |  |
| `repGerAprovacaoMat.dataAprov_ApPedM` | query | string (date-time) |  |  |
| `repGerAprovacaoMat.codCargo_ApPedM` | query | string |  |  |
| `repGerAprovacaoMat.codDep_ApPedM` | query | string |  |  |
| `repGerAprovacaoMat.numJusAprov_ApPedM` | query | integer (int32) |  |  |
| `repGerAprovacaoMat.num_ApPedM` | query | integer (int32) |  |  |
| `repGerAprovacaoMat.s_Empresa_ApPedM` | query | string |  |  |
| `repGerAprovacaoMat.s_Obra_ApPedM` | query | string |  |  |
| `repGerAprovacaoMat.s_Insumo_ApPedM` | query | string |  |  |
| `repGerAprovacaoMat.s_NumPedido_ApPedM` | query | string |  |  |
| `repGerAprovacaoMat.s_ItemPed_ApPedM` | query | string |  |  |
| `repGerAprovacaoMat.s_UsrAprov_ApPedM` | query | string |  |  |
| `repGerAprovacaoMat.s_DataAprov_ApPedM` | query | string |  |  |
| `repGerAprovacaoMat.s_CodCargo_ApPedM` | query | string |  |  |
| `repGerAprovacaoMat.s_CodDep_ApPedM` | query | string |  |  |
| `repGerAprovacaoMat.s_NumJusAprov_ApPedM` | query | string |  |  |
| `repGerAprovacaoMat.s_Num_ApPedM` | query | string |  |  |
| `repGerAprovacaoMat.querySource` | query | string |  |  |
| `repGerAprovacaoMat.mappingName` | query | string |  |  |
| `repGerAprovacaoMat.schemaGlobal` | query | string |  |  |
| `repGerAprovacaoMat.schemaTableView` | query | string |  |  |
| `repGerAprovacaoMat.schemaStoredProcedure` | query | string |  |  |
| `repGerAprovacaoMat.notRecommendedConnection.connectionString` | query | string |  |  |
| `repGerAprovacaoMat.notRecommendedConnection.commandTimeout` | query | integer (int32) |  |  |
| `repGerAprovacaoMat.notRecommendedConnection.connectionTimeout` | query | integer (int32) |  |  |
| `repGerAprovacaoMat.notRecommendedConnection.defaultDatabase` | query | string |  |  |
| `repGerAprovacaoMat.notRecommendedConnection.isolationLevel` | query | integer (int32) — valores possíveis: 16, 256, 256, 4096, 4096, 65536, 1048576, 1048576, -1 |  |  |
| `repGerAprovacaoMat.notRecommendedConnection.attributes` | query | integer (int32) |  |  |
| `repGerAprovacaoMat.notRecommendedConnection.cursorLocation` | query | integer (int32) — valores possíveis: 1, 2, 3, 3 |  |  |
| `repGerAprovacaoMat.notRecommendedConnection.mode` | query | integer (int32) — valores possíveis: 0, 1, 2, 3, 4, 8, 12, 16, 4194304 |  |  |
| `repGerAprovacaoMat.notRecommendedConnection.provider` | query | string |  |  |
| `repGerAprovacaoMat.connectionString` | query | string |  |  |
| `repGerAprovacaoMat.connectionStringConfig` | query | string |  |  |
| `repGerAprovacaoMat.filter` | query | string |  |  |
| `repGerAprovacaoMat.sort` | query | string |  |  |
| `repGerAprovacaoServ.stringFormat` | query | string |  |  |
| `repGerAprovacaoServ.numPedido_ApPedS` | query | integer (int32) |  |  |
| `repGerAprovacaoServ.empresa_ApPedS` | query | integer (int32) |  |  |
| `repGerAprovacaoServ.obra_ApPedS` | query | string |  |  |
| `repGerAprovacaoServ.serv_ApPedS` | query | string |  |  |
| `repGerAprovacaoServ.usrAprov_ApPedS` | query | string |  |  |
| `repGerAprovacaoServ.dataAprov_ApPedS` | query | string (date-time) |  |  |
| `repGerAprovacaoServ.codCargo_ApPedS` | query | string |  |  |
| `repGerAprovacaoServ.codDep_ApPedS` | query | string |  |  |
| `repGerAprovacaoServ.numJusAprov_ApPedS` | query | integer (int32) |  |  |
| `repGerAprovacaoServ.num_ApPedS` | query | integer (int32) |  |  |
| `repGerAprovacaoServ.s_NumPedido_ApPedS` | query | string |  |  |
| `repGerAprovacaoServ.s_Empresa_ApPedS` | query | string |  |  |
| `repGerAprovacaoServ.s_Obra_ApPedS` | query | string |  |  |
| `repGerAprovacaoServ.s_Serv_ApPedS` | query | string |  |  |
| `repGerAprovacaoServ.s_UsrAprov_ApPedS` | query | string |  |  |
| `repGerAprovacaoServ.s_DataAprov_ApPedS` | query | string |  |  |
| `repGerAprovacaoServ.s_CodCargo_ApPedS` | query | string |  |  |
| `repGerAprovacaoServ.s_CodDep_ApPedS` | query | string |  |  |
| `repGerAprovacaoServ.s_NumJusAprov_ApPedS` | query | string |  |  |
| `repGerAprovacaoServ.s_Num_ApPedS` | query | string |  |  |
| `repGerAprovacaoServ.querySource` | query | string |  |  |
| `repGerAprovacaoServ.mappingName` | query | string |  |  |
| `repGerAprovacaoServ.schemaGlobal` | query | string |  |  |
| `repGerAprovacaoServ.schemaTableView` | query | string |  |  |
| `repGerAprovacaoServ.schemaStoredProcedure` | query | string |  |  |
| `repGerAprovacaoServ.notRecommendedConnection.connectionString` | query | string |  |  |
| `repGerAprovacaoServ.notRecommendedConnection.commandTimeout` | query | integer (int32) |  |  |
| `repGerAprovacaoServ.notRecommendedConnection.connectionTimeout` | query | integer (int32) |  |  |
| `repGerAprovacaoServ.notRecommendedConnection.defaultDatabase` | query | string |  |  |
| `repGerAprovacaoServ.notRecommendedConnection.isolationLevel` | query | integer (int32) — valores possíveis: 16, 256, 256, 4096, 4096, 65536, 1048576, 1048576, -1 |  |  |
| `repGerAprovacaoServ.notRecommendedConnection.attributes` | query | integer (int32) |  |  |
| `repGerAprovacaoServ.notRecommendedConnection.cursorLocation` | query | integer (int32) — valores possíveis: 1, 2, 3, 3 |  |  |
| `repGerAprovacaoServ.notRecommendedConnection.mode` | query | integer (int32) — valores possíveis: 0, 1, 2, 3, 4, 8, 12, 16, 4194304 |  |  |
| `repGerAprovacaoServ.notRecommendedConnection.provider` | query | string |  |  |
| `repGerAprovacaoServ.connectionString` | query | string |  |  |
| `repGerAprovacaoServ.connectionStringConfig` | query | string |  |  |
| `repGerAprovacaoServ.filter` | query | string |  |  |
| `repGerAprovacaoServ.sort` | query | string |  |  |
| `Authorization` | header | string | ✓ | Token Authentication |
| `X-INTEGRATION-Authorization` | header | string | ✓ | Token De Integração |

### Respostas

| Status | Descrição | Esquema |
|---|---|---|
| 200 | OK | array de [`Globaltec.UAU.Comp.IntegracaoMobileAPI.ContratoMaterialServico.DTOs.GetEstruturaAprovacoesDTO`](#globaltecuaucompintegracaomobileapicontratomaterialservicodtosgetestruturaaprovacoesdto) |

---

## POST `/api/v{version}/ContratoMaterialServico/ConsultarContratoPorChave`

**Consultar contrato**

Definição Técnica:
1. Autenticar o usuário cliente URI + /api/v{version}/Autenticador/AutenticarUsuario
2. Preencher os parâmetros de request para uso do endpoint.
3. Retorna os dados do contrato.

Definição de Negócio:
1. Consulta contrato filtrando pela chave.

Link para Virtuau relacionado: https://ajuda.globaltec.com.br/virtuau/contrato-de-materiais-e-servicos/

### Parâmetros

| Nome | Em | Tipo | Obrigatório | Descrição |
|---|---|---|---|---|
| `version` | path | string | ✓ |  |
| `Authorization` | header | string | ✓ | Token Authentication |
| `X-INTEGRATION-Authorization` | header | string | ✓ | Token De Integração |

### Corpo da requisição

Obrigatório: ✓  
Esquema: [`UAUApi.Models.ContratoMaterialServico.ConsultarContratoPorChaveRequest`](#uauapimodelscontratomaterialservicoconsultarcontratoporchaverequest)

### Respostas

| Status | Descrição | Esquema |
|---|---|---|
| 200 | Contratos | array de [`UAUApi.Models.ContratoMaterialServico.Contratos`](#uauapimodelscontratomaterialservicocontratos) |
| 400 | Não foi possível realizar sua requisição. | [`UAUApi.ResponseHandler`](#uauapiresponsehandler) |
| 500 | Ocorreu um erro ao processar sua requisição. | [`UAUApi.ResponseHandler`](#uauapiresponsehandler) |

---

## POST `/api/v{version}/ContratoMaterialServico/ConsultarContratoPorFornecedor`

**Consultar contratos por fornecedor**

Definição Técnica:
1. Autenticar o usuário cliente URI + /api/v{version}/Autenticador/AutenticarUsuario
2. Preencher os parâmetros de request para uso do endpoint.

Definição de Negócio:
1. Consulta os contratos de um fornecedor.

Link para Virtuau relacionado: https://ajuda.globaltec.com.br/virtuau/contrato-de-materiais-e-servicos/

### Parâmetros

| Nome | Em | Tipo | Obrigatório | Descrição |
|---|---|---|---|---|
| `version` | path | string | ✓ |  |
| `Authorization` | header | string | ✓ | Token Authentication |
| `X-INTEGRATION-Authorization` | header | string | ✓ | Token De Integração |

### Corpo da requisição

Obrigatório: ✓  
Esquema: [`UAUApi.Models.ContratoMaterialServico.ConsultarContratoPorFornecedor`](#uauapimodelscontratomaterialservicoconsultarcontratoporfornecedor)

### Respostas

| Status | Descrição | Esquema |
|---|---|---|
| 200 | Contratos | array de [`UAUApi.Models.ContratoMaterialServico.Contratos`](#uauapimodelscontratomaterialservicocontratos) |
| 400 | Não foi possível realizar sua requisição. | [`UAUApi.ResponseHandler`](#uauapiresponsehandler) |
| 500 | Ocorreu um erro ao processar sua requisição. | [`UAUApi.ResponseHandler`](#uauapiresponsehandler) |

---

## POST `/api/v{version}/ContratoMaterialServico/ConsultarContratoPorServicoMaterial`

**Consultar contrato por serviço/material e empresa**

Definição Técnica:
1. Autenticar o usuário cliente URI + /api/v{version}/Autenticador/AutenticarUsuario
2. Preencher os parâmetros de request para uso do endpoint.

Definição de Negócio:
1. Consulta contrato filtrando por:
    1. Empresa;
    2. Serviço ou material;
    
Link para Virtuau relacionado: https://ajuda.globaltec.com.br/virtuau/contrato-de-materiais-e-servicos/

### Parâmetros

| Nome | Em | Tipo | Obrigatório | Descrição |
|---|---|---|---|---|
| `version` | path | string | ✓ |  |
| `Authorization` | header | string | ✓ | Token Authentication |
| `X-INTEGRATION-Authorization` | header | string | ✓ | Token De Integração |

### Corpo da requisição

Obrigatório: ✓  
Esquema: [`UAUApi.Models.ContratoMaterialServico.ConsultarContratoPorServicoMaterialRequest`](#uauapimodelscontratomaterialservicoconsultarcontratoporservicomaterialrequest)

### Respostas

| Status | Descrição | Esquema |
|---|---|---|
| 200 | Itens de contrato | array de [`UAUApi.Models.ContratoMaterialServico.Contratos`](#uauapimodelscontratomaterialservicocontratos) |
| 400 | Não foi possível realizar sua requisição. | [`UAUApi.ResponseHandler`](#uauapiresponsehandler) |
| 500 | Ocorreu um erro ao processar sua requisição. | [`UAUApi.ResponseHandler`](#uauapiresponsehandler) |

---

## POST `/api/v{version}/ContratoMaterialServico/ConsultarContratosItensVinculadoOrcamento`

**Consultar os contratos e itens de contratos de material/serviço que estejam vinculados a um determinado orçamento de serviço**

Definição Técnica:
1. Autenticar o usuário cliente URI + /api/v{version}/Autenticador/AutenticarUsuario
2. Preencher os parâmetros de request para uso do endpoint.
3. Retorna os dados dos itens de contratos vinculados a um determinado orçamento de serviço.

Definição de Negócio:
1. Consultar os contratos e itens de contratos de material/serviço que estejam vinculados a um determinado orçamento de serviço.
2. Para retornar apenas os itens de contratos que estejam aprovados, o parâmetro "somenteContratosAprovados" deve ser passado como TRUE.

Link para Virtuau relacionado: https://ajuda.globaltec.com.br/virtuau/contrato-de-materiais-e-servicos/

### Parâmetros

| Nome | Em | Tipo | Obrigatório | Descrição |
|---|---|---|---|---|
| `version` | path | string | ✓ |  |
| `Authorization` | header | string | ✓ | Token Authentication |
| `X-INTEGRATION-Authorization` | header | string | ✓ | Token De Integração |

### Corpo da requisição

Obrigatório: ✓  
Esquema: [`UAUApi.Models.ContratoMaterialServico.ConsultarContratosItensVinculadoOrcamentoRequest`](#uauapimodelscontratomaterialservicoconsultarcontratositensvinculadoorcamentorequest)

### Respostas

| Status | Descrição | Esquema |
|---|---|---|
| 200 | Consultar os itens  do vinculo com o orçamento | array de [`UAUApi.Models.ItensVinculoOrcamento`](#uauapimodelsitensvinculoorcamento) |
| 400 | Não foi possível realizar sua ação. | [`UAUApi.ResponseHandler`](#uauapiresponsehandler) |
| 500 | Ocorreu um erro ao processar sua ação. | [`UAUApi.ResponseHandler`](#uauapiresponsehandler) |

---

## POST `/api/v{version}/ContratoMaterialServico/ConsultarItensContrato`

**Consultar itens de contrato**

Definição Técnica:
1. Autenticar o usuário cliente URI + /api/v{version}/Autenticador/AutenticarUsuario
2. Preencher os parâmetros de request para uso do endpoint.

Definição de Negócio:
1. Consultar itens presentes em um contrato.

### Parâmetros

| Nome | Em | Tipo | Obrigatório | Descrição |
|---|---|---|---|---|
| `version` | path | string | ✓ |  |
| `Authorization` | header | string | ✓ | Token Authentication |
| `X-INTEGRATION-Authorization` | header | string | ✓ | Token De Integração |

### Corpo da requisição

Obrigatório: ✓  
Esquema: [`UAUApi.Models.ContratoMaterialServico.ConsultarItensContratoRequest`](#uauapimodelscontratomaterialservicoconsultaritenscontratorequest)

### Respostas

| Status | Descrição | Esquema |
|---|---|---|
| 200 | Itens de contrato | array de [`UAUApi.Models.ContratoMaterialServico.ItensContrato`](#uauapimodelscontratomaterialservicoitenscontrato) |
| 400 | Não foi possível realizar sua requisição. | [`UAUApi.ResponseHandler`](#uauapiresponsehandler) |
| 500 | Ocorreu um erro ao processar sua requisição. | [`UAUApi.ResponseHandler`](#uauapiresponsehandler) |

---

## POST `/api/v{version}/ContratoMaterialServico/ConsultarItensVinculoOrcamentoServico`

**Consultar os itens  do vinculo com o orçamento - SERVIÇOS**

Definição Técnica:
1. Autenticar o usuário cliente URI + /api/v{version}/Autenticador/AutenticarUsuario
2. Preencher os parâmetros de request para uso do endpoint.
3. Retorna os dados dos itens de contratos vinculados a um determinado orçamento de serviço.

Definição de Negócio:
1. Consultar os itens de contratos de material/serviço que estejam vinculados a um determinado orçamento de serviço.
2. Para retornar apenas os itens de contratos que estejam aprovados, o parâmetro "somenteContratosAprovados" deve ser passado como TRUE.

Link para Virtuau relacionado: https://ajuda.globaltec.com.br/virtuau/contrato-de-materiais-e-servicos/

### Parâmetros

| Nome | Em | Tipo | Obrigatório | Descrição |
|---|---|---|---|---|
| `version` | path | string | ✓ |  |
| `Authorization` | header | string | ✓ | Token Authentication |
| `X-INTEGRATION-Authorization` | header | string | ✓ | Token De Integração |

### Corpo da requisição

Obrigatório: ✓  
Esquema: [`UAUApi.Models.ContratoMaterialServico.ConsultarItensVinculoOrcamentoServicoRequest`](#uauapimodelscontratomaterialservicoconsultaritensvinculoorcamentoservicorequest)

### Respostas

| Status | Descrição | Esquema |
|---|---|---|
| 200 | Consultar os itens  do vinculo com o orçamento - SERVIÇOS | array de [`UAUApi.Models.ContratoVinculoPlanejamentoServico`](#uauapimodelscontratovinculoplanejamentoservico) |
| 400 | Não foi possível realizar sua ação. | [`UAUApi.ResponseHandler`](#uauapiresponsehandler) |
| 500 | Ocorreu um erro ao processar sua ação. | [`UAUApi.ResponseHandler`](#uauapiresponsehandler) |

---

## POST `/api/v{version}/ContratoMaterialServico/ConsultarItensVinculoPlanejamentoServico`

**Consultar os itens  do vinculo com o planejamento - SERVIÇOS**

### Parâmetros

| Nome | Em | Tipo | Obrigatório | Descrição |
|---|---|---|---|---|
| `version` | path | string | ✓ |  |
| `Authorization` | header | string | ✓ | Token Authentication |
| `X-INTEGRATION-Authorization` | header | string | ✓ | Token De Integração |

### Corpo da requisição

Obrigatório: ✓  
Esquema: [`UAUApi.Models.ContratoMaterialServico.ConsultarItensVinculoPlanejamentoServicoRequest`](#uauapimodelscontratomaterialservicoconsultaritensvinculoplanejamentoservicorequest)

### Respostas

| Status | Descrição | Esquema |
|---|---|---|
| 200 | onsultar os itens  do vinculo com o planejamento - SERVIÇOS | array de [`UAUApi.Models.ContratoVinculoPlanejamentoServico`](#uauapimodelscontratovinculoplanejamentoservico) |
| 400 | Não foi possível realizar sua ação. | [`UAUApi.ResponseHandler`](#uauapiresponsehandler) |
| 500 | Ocorreu um erro ao processar sua ação. | [`UAUApi.ResponseHandler`](#uauapiresponsehandler) |

---

## POST `/api/v{version}/ContratoMaterialServico/ConsultarSaldoReajustadoPorItemContrato`

**- Método com finalidade de consultar valores aprovados e saldo reajustado de itens do contrato.**

Definição Técnica:
1. Autenticar o usuário cliente URI + /api/v{version}/Autenticador/AutenticarUsuario
2. Preencher os parâmetros de request para uso do endpoint.

Definição de Negócio:
1. Consultar valores aprovados e saldo reajustado de itens do contrato.
2. Consulta contrato filtrando por:
    1. Empresa (obrigatório)
    2. Obra;
    3. Situacoes (pode ser informado uma lista de situações): 
        - 0 - Andamento
        - 1 - Paralisado
        - 2 - Cancelado
        - 3 - Concluído
        - 4 - Em encerramento
    4. Contratos (pode ser informada uma lista de contratos);
    
Link para Virtuau relacionado: https://ajuda.globaltec.com.br/virtuau/contrato-de-materiais-e-servicos/

### Parâmetros

| Nome | Em | Tipo | Obrigatório | Descrição |
|---|---|---|---|---|
| `version` | path | string | ✓ |  |
| `Authorization` | header | string | ✓ | Token Authentication |
| `X-INTEGRATION-Authorization` | header | string | ✓ | Token De Integração |

### Corpo da requisição

Obrigatório: ✓  
Esquema: [`UAUApi.Models.ContratoMaterialServico.ConsultarItensContratoEmpresaRequest`](#uauapimodelscontratomaterialservicoconsultaritenscontratoempresarequest)

### Respostas

| Status | Descrição | Esquema |
|---|---|---|
| 200 | Itens de contrato  | array de [`Globaltec.UAU.Obras.ContratoDetail`](#globaltecuauobrascontratodetail) |
| 400 | Não foi possível realizar sua requisição. | [`UAUApi.ResponseHandler`](#uauapiresponsehandler) |
| 500 | Ocorreu um erro ao processar sua requisição. | [`UAUApi.ResponseHandler`](#uauapiresponsehandler) |

---

## Esquemas

### Globaltec.UAU.Obras.ContratoDetail

| Propriedade | Tipo | Obrigatório | Descrição |
|---|---|---|---|
| `Empresa` | integer (int32) |  |  |
| `Obra` | string |  |  |
| `Contrato` | integer (int32) |  |  |
| `Objeto` | string |  |  |
| `DataCriacao` | string (date-time) |  |  |
| `CodContratado` | integer (int32) |  |  |
| `Contratado` | string |  |  |
| `Situacao` | integer (int32) |  |  |
| `Itens` | array de [`Globaltec.UAU.Obras.ItensContratoComSI`](#globaltecuauobrasitenscontratocomsi) |  |  |

### Globaltec.UAU.Obras.ItensContratoComSI

| Propriedade | Tipo | Obrigatório | Descrição |
|---|---|---|---|
| `Item` | integer (int32) |  |  |
| `Codigo` | string |  |  |
| `Descricao` | string |  |  |
| `Unid` | string |  |  |
| `Plano` | integer (int32) |  |  |
| `Qtde` | number (double) |  |  |
| `Preco_Unit` | number (double) |  |  |
| `Aprovadas` | number (double) |  |  |
| `Pagas` | number (double) |  |  |
| `Saldo_reajustado` | number (double) |  |  |
| `SubTotal` | number (double) |  |  |
| `Vinculos` | array de [`Globaltec.UAU.Obras.VinculosItemContDetail`](#globaltecuauobrasvinculositemcontdetail) |  |  |

### Globaltec.UAU.Obras.VinculosItemContDetail

| Propriedade | Tipo | Obrigatório | Descrição |
|---|---|---|---|
| `ItemPL` | string |  |  |
| `Cod_Servico` | string |  |  |
| `Servico` | string |  |  |
| `Codigo_InsumoPL` | string |  |  |
| `InsumoPL` | string |  |  |
| `Produto` | integer (int32) |  |  |
| `ContratoPL` | integer (int32) |  |  |
| `Total_Vinculado` | number (double) |  |  |
| `Valor_Aprovado` | number (double) |  |  |
| `Saldo` | number (double) |  |  |
| `Saldo_Reajustado` | number (double) |  |  |

### UAUApi.Models.ContratoMaterialServico.ConsultarItensContratoEmpresaRequest

| Propriedade | Tipo | Obrigatório | Descrição |
|---|---|---|---|
| `empresa` | integer (int32) | ✓ | Código da empresa do contrato. |
| `obra` | string |  | Código da obra. |
| `contratos` | array de integer (int32) |  | Códigos dos contratos. |
| `situacoes` | array de integer (int32) |  | Códigos das situações. |

### UAUApi.Models.ContratoMaterialServico.ConsultarItensVinculoPlanejamentoServicoRequest

| Propriedade | Tipo | Obrigatório | Descrição |
|---|---|---|---|
| `empresa` | integer (int32) |  | Código da empresa do contrato. |
| `obra` | string |  | Código da obra. |
| `item` | string |  | Código do item. |
| `servico` | string |  | Código do serviço. |
| `produto` | integer (int32) |  | Código do produto |
| `contrato` | integer (int32) |  | Código do contrato no planejamento |

### UAUApi.Models.ContratoVinculoPlanejamentoServico

| Propriedade | Tipo | Obrigatório | Descrição |
|---|---|---|---|
| `contrato_servico` | integer (int32) |  |  |
| `codigo_pessoa` | string |  |  |
| `nome_pessoa` | string |  |  |
| `objeto_contrato` | string |  |  |

### UAUApi.Models.ContratoMaterialServico.ConsultarItensVinculoOrcamentoServicoRequest

| Propriedade | Tipo | Obrigatório | Descrição |
|---|---|---|---|
| `empresa` | integer (int32) |  | Código da empresa do contrato. |
| `obra` | string |  | Código da obra. |
| `item` | string |  | Código do item. |
| `servico` | string |  | Código do serviço. |
| `orcamento` | integer (int32) |  | Código do orçamento |
| `somenteContratosAprovados` | boolean |  | Indica se deseja retornar somente os itens de contratos que estejam aprovados |

### UAUApi.Models.ContratoMaterialServico.ItensContrato

| Propriedade | Tipo | Obrigatório | Descrição |
|---|---|---|---|
| `Empresa_itens` | integer (int32) |  |  |
| `Contrato_itens` | integer (int32) |  |  |
| `Item_itens` | integer (int32) |  |  |
| `Serv_itens` | string |  |  |
| `Descr_itens` | string |  |  |
| `Unid_itens` | string |  |  |
| `Qtde_itens` | number (double) |  |  |
| `Preco_itens` | number (double) |  |  |
| `Origem_itens` | integer (int32) |  |  |
| `Reaj_itens` | integer (int32) |  |  |
| `Cap_itens` | string |  |  |
| `Categ_itens` | string |  |  |
| `TipoServMat_Itens` | boolean |  |  |
| `SaldoMedicao_Itens` | number (double) |  |  |

### UAUApi.Models.ContratoMaterialServico.ConsultarItensContratoRequest

| Propriedade | Tipo | Obrigatório | Descrição |
|---|---|---|---|
| `empresa` | integer (int32) |  | Código da empresa do contrato. |
| `contrato` | integer (int32) |  | Código do contrato. |

### UAUApi.Models.ItensVinculoOrcamento

| Propriedade | Tipo | Obrigatório | Descrição |
|---|---|---|---|
| `contrato_servico` | integer (int32) |  |  |
| `codigo_pessoa` | string |  |  |
| `nome_pessoa` | string |  |  |
| `objeto_contrato` | string |  |  |
| `codigo_servico` | string |  |  |
| `item_orcamento` | string |  |  |
| `item_contrato` | string |  |  |

### UAUApi.Models.ContratoMaterialServico.ConsultarContratosItensVinculadoOrcamentoRequest

| Propriedade | Tipo | Obrigatório | Descrição |
|---|---|---|---|
| `empresa` | integer (int32) |  | Código da empresa do contrato. |
| `obra` | string |  | Código da obra. |
| `orcamento` | integer (int32) |  | Código do orçamento |
| `somenteContratosAprovados` | boolean |  | Indica se deseja retornar somente os itens de contratos que estejam aprovados |

### UAUApi.Models.ContratoMaterialServico.ConsultarContratoPorServicoMaterialRequest

| Propriedade | Tipo | Obrigatório | Descrição |
|---|---|---|---|
| `empresa` | integer (int32) |  | Código da empresa do contrato. |
| `servicoMaterial` | string |  | Código do serviço ou material do contrato. |

### UAUApi.Models.ContratoMaterialServico.ConsultarContratoPorFornecedor

| Propriedade | Tipo | Obrigatório | Descrição |
|---|---|---|---|
| `fornecedor` | integer (int32) | ✓ | Código do fornecedor do contrato. |

### UAUApi.ResponseHandler

| Propriedade | Tipo | Obrigatório | Descrição |
|---|---|---|---|
| `Detalhe` | string |  | Detalhamento da Exception StrackTrace |
| `Mensagem` | string |  | Mensagem da Exception |
| `Descricao` | string |  | Descrição personalizada |

### UAUApi.Models.ContratoMaterialServico.Contratos

| Propriedade | Tipo | Obrigatório | Descrição |
|---|---|---|---|
| `Empresa_cont` | integer (int32) |  | Código da empresa |
| `Cod_cont` | integer (int32) |  | Código do contrato |
| `Obra_cont` | string |  | Código da obra |
| `CodPes_cont` | integer (int32) |  | Código do fornecedor |
| `DescrPes_cont` | string |  | Descrição/Nome do fornecedor do contrato |
| `cpf_pes` | string |  | CNPJ do fornecedor do contrato |
| `Objeto_cont` | string |  | Descrição/Objeto do contrato |
| `DtCriacao_cont` | string (date-time) |  | Data de criação do contrato |
| `DtInicio_cont` | string (date-time) |  | Data de início do contrato |
| `DtFim_cont` | string (date-time) |  | Data final do contrato |
| `Quem_cont` | string |  | Usuário quem registrou |
| `Situacao_cont` | integer (int32) |  | Situação do contrato, onde: 0 - Andamento; 1 - Paralisado; 2 - Cancelado; 3 - Concluído; 4 - Em encerramento |
| `Tipo_Cont` | string |  | Tipo do contrato |
| `Descr_TipCon` | string |  | Descrição do tipo do contrato |
| `Estagio_Cont` | string |  | Estágio do contrato |
| `Obs_cont` | string |  | Observação do contrato |
| `Status_cont` | integer (int32) |  | Status do contrato, onde: 0 - Não aprovado; 1 - Aprovado; 2 - Em aditivo |
| `CondPag_cont` | string |  | Condição do pagamento |
| `EndPag_cont` | string |  | Endereço de pagamento |
| `CondEnt_cont` | string |  | Condição da entrega |
| `TipoPgto_cont` | integer (int32) |  | Tipo do pagamento |
| `Anexos_Cont` | integer (int32) |  | Anexos no contrato |
| `Controle_cont` | integer (int32) |  | Informa que o contrato está configurado para trabalhar com múltiplos fornecedores/contratados, onde 0 - Somente um fornecedor; 3 - Múltiplos fornecedores/contratados |
| `TipoCont_cont` | integer (int32) |  | Tipo do contrato 0 - Unidirecional 1 - Bidirecional |
| `EmpPaga_cont` | integer (int32) |  | Empresa pagadora |
| `EmpFatura_cont` | integer (int32) |  | Empresa faturada |
| `TipoServMat_Cont` | integer (int32) |  | Indicador de tipo de controle do contrato, onde: 0 - Serviço; 1 - Material; 2 - Misto; |
| `CasaDecQtde_Cont` | integer (int32) |  | Quantidade de casas decimais para a quantidade |
| `CasaDecPreco_Cont` | integer (int32) |  | Quantidade de casas decimais para o preço |
| `MotivoAlter_cont` | string |  | Motivo da alteração do contrato |
| `CarenciaBloqueioPrazo_cont` | integer (int32) |  | Prazo de carência para bloqueio |
| `Banco_cont` | integer (int32) |  | Número do banco associado ao contrato |
| `Conta_cont` | string |  | Número da conta associada ao contrato |
| `CategMovFin_cont` | string |  | Categoria de movimentação financeira |
| `ContratoAtual_cont` | boolean |  | Indicador de utilização de configuração de tributos |
| `AdiantParcial_cont` | boolean |  | Adiantamento de parcela |

### UAUApi.Models.ContratoMaterialServico.ConsultarContratoPorChaveRequest

| Propriedade | Tipo | Obrigatório | Descrição |
|---|---|---|---|
| `empresa` | integer (int32) | ✓ | Código da empresa do contrato. |
| `contrato` | integer (int32) | ✓ | Código do contrato. |

### Globaltec.UAU.Comp.IntegracaoMobileAPI.ContratoMaterialServico.DTOs.GetEstruturaAprovacoesDTO

| Propriedade | Tipo | Obrigatório | Descrição |
|---|---|---|---|
| `Sequencia` | integer (int32) |  |  |
| `UsuarioAprov` | string |  |  |
| `DataAprov` | string |  |  |
| `Cod_dep` | string |  |  |
| `Desc_dep` | string |  |  |
| `Cod_cargo` | string |  |  |
| `Desc_cargo` | string |  |  |
