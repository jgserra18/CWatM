# -------------------------------------------------------------------------
# Name:        Land Cover Type module
# Purpose:
#
# Author:      PB
#
# Created:     15/07/2016
# Copyright:   (c) PB 2016
# -------------------------------------------------------------------------

from cwatm.management_modules.data_handling import *


class landcoverType(object):

    """
    LAND COVER TYPE

    runs the 6 land cover types through soil procedures

    This routine calls the soil routine for each land cover type


    **Global variables**

    ====================  ================================================================================  =========
    Variable [self.var]   Description                                                                       Unit     
    ====================  ================================================================================  =========
    load_initial                                                                                                     
    sum_gwRecharge        groundwater recharge                                                              m        
    modflow               Flag: True if modflow_coupling = True in settings file                            --       
    modflow_timestep      Chosen ModFlow model timestep (1day, 7days, 30days…)                                       
    sumed_sum_gwRecharge                                                                                             
    GWVolumeVariation                                                                                                
    snowEvap              total evaporation from snow for a snow layers                                     m        
    maxGWCapRise          influence of capillary rise above groundwater level                               m        
    minInterceptCap       Maximum interception read from file for forest and grassland land cover           m        
    interceptStor         simulated vegetation interception storage                                         m        
    dynamicLandcover                                                                                                 
    landcoverSum                                                                                                     
    act_SurfaceWaterAbst                                                                                             
    sum_interceptStor     Total of simulated vegetation interception storage including all landcover types  m        
    fracVegCover          Fraction of area covered by the corresponding landcover type                               
    minCropKC             minimum crop factor (default 0.2)                                                 --       
    minTopWaterLayer                                                                                                 
    rootFraction1                                                                                                    
    maxRootDepth                                                                                                     
    rootDepth                                                                                                        
    KSat1                                                                                                            
    KSat2                                                                                                            
    KSat3                                                                                                            
    alpha1                                                                                                           
    alpha2                                                                                                           
    alpha3                                                                                                           
    lambda1                                                                                                          
    lambda2                                                                                                          
    lambda3                                                                                                          
    thetas1                                                                                                          
    thetas2                                                                                                          
    thetas3                                                                                                          
    thetar1                                                                                                          
    thetar2                                                                                                          
    thetar3                                                                                                          
    genuM1                                                                                                           
    genuM2                                                                                                           
    genuM3                                                                                                           
    genuInvM1                                                                                                        
    genuInvM2                                                                                                        
    genuInvM3                                                                                                        
    genuInvN1                                                                                                        
    genuInvN2                                                                                                        
    genuInvN3                                                                                                        
    invAlpha1                                                                                                        
    invAlpha2                                                                                                        
    invAlpha3                                                                                                        
    ws1                   Maximum storage capacity in layer 1                                               m        
    ws2                   Maximum storage capacity in layer 2                                               m        
    ws3                   Maximum storage capacity in layer 3                                               m        
    wres1                 Residual storage capacity in layer 1                                              m        
    wres2                 Residual storage capacity in layer 2                                              m        
    wres3                 Residual storage capacity in layer 3                                              m        
    wrange1                                                                                                          
    wrange2                                                                                                          
    wrange3                                                                                                          
    wfc1                  Soil moisture at field capacity in layer 1                                                 
    wfc2                  Soil moisture at field capacity in layer 2                                                 
    wfc3                  Soil moisture at field capacity in layer 3                                                 
    wwp1                  Soil moisture at wilting point in layer 1                                                  
    wwp2                  Soil moisture at wilting point in layer 2                                                  
    wwp3                  Soil moisture at wilting point in layer 3                                                  
    kUnSat3FC                                                                                                        
    kunSatFC12                                                                                                       
    kunSatFC23                                                                                                       
    cropCoefficientNC_fi                                                                                             
    interceptCapNC_filen                                                                                             
    coverFractionNC_file                                                                                             
    sum_topwater          quantity of water on the soil (flooding) (weighted sum for all landcover types)   m        
    sum_soil                                                                                                         
    sum_w1                                                                                                           
    sum_w2                                                                                                           
    sum_w3                                                                                                           
    totalSto              Total soil,snow and vegetation storage for each cell including all landcover typ  m        
    arnoBetaOro                                                                                                      
    arnoBeta                                                                                                         
    adjRoot                                                                                                          
    maxtopwater           maximum heigth of topwater                                                        m        
    totAvlWater                                                                                                      
    presumed_sum_gwRecha  Previous groundwater recharge [m/timestep] (used for the ModFlow version)         m        
    pretotalSto           Previous totalSto                                                                 m        
    sum_actBareSoilEvap                                                                                              
    sum_openWaterEvap                                                                                                
    addtoevapotrans                                                                                                  
    sum_runoff            Runoff above the soil, more interflow, including all landcover types              m        
    sum_directRunoff                                                                                                 
    sum_interflow                                                                                                    
    sum_availWaterInfilt                                                                                             
    sum_capRiseFromGW     capillar rise from groundwater to 3rd soil layer (summed up for all land cover c  m        
    sum_act_irrConsumpti                                                                                             
    sum_perc3toGW         percolation from 3rd soil layer to groundwater (summed up for all land cover cla  m        
    sum_prefFlow          preferential flow from soil to groundwater (summed up for all land cover classes  m        
    act_irrWithdrawal                                                                                                
    act_nonIrrConsumptio                                                                                             
    returnFlow                                                                                                       
    cellArea              Cell area [m²] of each simulated mesh                                                      
    baseflow              simulated baseflow (= groundwater discharge to river)                             m        
    Precipitation         Precipitation (input for the model)                                               m        
    coverTypes            land cover types - forest - grassland - irrPaddy - irrNonPaddy - water - sealed   --       
    Rain                  Precipitation less snow                                                           m        
    SnowMelt              total snow melt from all layers                                                   m        
    SnowCover             snow cover (sum over all layers)                                                  m        
    ElevationStD                                                                                                     
    prevSnowCover         snow cover of previous day (only for water balance)                               m        
    soilLayers            Number of soil layers                                                             --       
    soildepth             Thickness of the first soil layer                                                 m        
    soildepth12           Total thickness of layer 2 and 3                                                  m        
    w1                    Simulated water storage in the layer 1                                            m        
    w2                    Simulated water storage in the layer 2                                            m        
    w3                    Simulated water storage in the layer 3                                            m        
    topwater              quantity of water above the soil (flooding)                                       m        
    totalET               Total evapotranspiration for each cell including all landcover types              m        
    sum_actTransTotal                                                                                                
    sum_interceptEvap                                                                                                
    ====================  ================================================================================  =========

    **Functions**
    """

    def __init__(self, model):
        self.var = model.var
        self.model = model

    # noinspection PyTypeChecker
    def initial(self):
        """
        Initial part of the land cover type module
        Initialise the six land cover types

        * Forest No.0
        * Grasland/non irrigated land No.1
        * Paddy irrigation No.2
        * non-Paddy irrigation No.3
        * Sealed area No.4
        * Water covered area No.5

        And initialize the soil variables
        """

        # make land cover change from year to year or fix it to 1 year
        if returnBool('dynamicLandcover'):
            self.var.dynamicLandcover = True
        else:
            self.var.dynamicLandcover = False


        self.var.coverTypes= list(map(str.strip, cbinding("coverTypes").split(",")))
        landcoverAll = ['fracVegCover','interceptStor','interceptCap','availWaterInfiltration','interceptEvap',
                        'directRunoff', 'openWaterEvap']
        for variable in landcoverAll:  vars(self.var)[variable] = np.tile(globals.inZero, (6, 1))

        landcoverPara = ['minInterceptCap','cropDeplFactor','rootFraction1',
                         'maxRootDepth', 'topWaterLayer','interflow',
                         'cropCoefficientNC_filename', 'interceptCapNC_filename','coverFractionNC_filename']
        # arrays stored as list not as numpy, because it can contain strings, single parameters or arrays
        # list is filled with append afterwards
        for variable in landcoverPara: vars(self.var)[variable] = []

        # fraction (m2) of a certain irrigation type over (only) total irrigation area ; will be assigned by the landSurface module
        # output variable per land cover class
        landcoverVars = ['irrTypeFracOverIrr','fractionArea','totAvlWater','cropKC',
                         'effSatAt50',  'effPoreSizeBetaAt50', 'rootZoneWaterStorageMin','rootZoneWaterStorageRange',
                         'totalPotET','potTranspiration','soilWaterStorage',
                         'infiltration','actBareSoilEvap','landSurfaceRunoff','actTransTotal',
                         'gwRecharge','interflow','actualET','pot_irrConsumption','act_irrConsumption','irrDemand',
                         'topWaterLayer',
                         'perc3toGW','capRiseFromGW','netPercUpper','netPerc','prefFlow']
     
        # for 6 landcover types
        for variable in landcoverVars:  vars(self.var)[variable] = np.tile(globals.inZero,(6,1))

        #for 4 landcover types with soil underneath
        landcoverVarsSoil = ['arnoBeta','rootZoneWaterStorageCap','rootZoneWaterStorageCap12','perc1to2','perc2to3','theta1','theta2','theta3']
        for variable in landcoverVarsSoil:  vars(self.var)[variable] = np.tile(globals.inZero,(4,1))

        soilVars = ['adjRoot','perc','capRise','rootDepth','storCap']
        # For 3 soil layers and 4 landcover types
        for variable in soilVars:  vars(self.var)[variable]= np.tile(globals.inZero,(self.var.soilLayers,4,1))

        # set aggregated storages to zero
        self.var.landcoverSum = ['interceptStor', 'interflow',
                         'directRunoff', 'totalPotET', 'potTranspiration', 'availWaterInfiltration',
                         'interceptEvap', 'infiltration', 'actBareSoilEvap', 'landSurfaceRunoff', 'actTransTotal', 'gwRecharge',
                          'openWaterEvap','capRiseFromGW','perc3toGW','prefFlow', 'actualET', 'act_irrConsumption']
        for variable in self.var.landcoverSum: vars(self.var)["sum_"+variable] = globals.inZero.copy()

        # for three soil layers
        soilVars = ['w1','w2','w3']
        for variable in soilVars: vars(self.var)[variable] = np.tile(globals.inZero,(4,1))
        for variable in soilVars: vars(self.var)["sum_" + variable] = globals.inZero.copy()


        self.var.totalET = globals.inZero.copy()
        self.var.act_SurfaceWaterAbstract = globals.inZero.copy()

        # ----------------------------------------------------------
        # Load initial values and calculate basic soil parameters which are not changed in time

        self.dynamic_fracIrrigation(init=True, dynamic = True)
        i = 0
        for coverType in self.var.coverTypes:
            self.var.minInterceptCap.append(loadmap(coverType + "_minInterceptCap"))
            # init values
            if coverType in ['forest', 'grassland', 'irrPaddy', 'irrNonPaddy','sealed']:
                self.var.interceptStor[i] = self.var.load_initial(coverType + "_interceptStor")

            # summarize the following initial storages:
            self.var.sum_interceptStor += self.var.fracVegCover[i] * self.var.interceptStor[i]
            i += 1



        self.var.minCropKC= loadmap('minCropKC')
        self.var.minTopWaterLayer = loadmap("minTopWaterLayer")
        self.var.maxGWCapRise = loadmap("maxGWCapRise")

        i = 0
        for coverType in self.var.coverTypes[:4]:
            # other paramater values
            # b coefficient of soil water storage capacity distribution
            #self.var.minTopWaterLayer.append(loadmap(coverType + "_minTopWaterLayer"))
            #self.var.minCropKC.append(loadmap(coverType + "_minCropKC"))

            #self.var.minInterceptCap.append(loadmap(coverType + "_minInterceptCap"))
            #self.var.cropDeplFactor.append(loadmap(coverType + "_cropDeplFactor"))
            # parameter values

            self.var.rootFraction1.append(loadmap(coverType + "_rootFraction1"))
            #self.var.rootFraction2.append(loadmap(coverType + "_rootFraction2"))

            soildepth_factor = loadmap('soildepth_factor')
            self.var.maxRootDepth.append(loadmap(coverType + "_maxRootDepth")* soildepth_factor)

            i += 1


        i = 0
        for coverType in self.var.coverTypes[:4]:
            # calculate rootdepth for each soillayer and each land cover class
            # self.var.rootDepth[0][i] = np.minimum(self.var.soildepth[0], self.var.maxRootDepth[i])
            self.var.rootDepth[0][i] = self.var.soildepth[0].copy()  # 0.05 m
            # if land cover = forest
            if coverType != 'grassland':
                # soil layer 1 = root max of land cover  - first soil layer
                h1 = np.maximum(self.var.soildepth[1], self.var.maxRootDepth[i] - self.var.soildepth[0])
                #
                self.var.rootDepth[1][i] = np.minimum(self.var.soildepth12 - 0.05, h1)
                # soil layer is minimim 0.05 m
                self.var.rootDepth[2][i] = np.maximum(0.05, self.var.soildepth12 - self.var.rootDepth[1][i])
            else:
                self.var.rootDepth[1][i] = self.var.soildepth[1].copy()
                self.var.rootDepth[2][i] = self.var.soildepth[2].copy()
            i += 1



        soilVars1 = ['KSat1','KSat2','KSat3','alpha1','alpha2','alpha3', 'lambda1','lambda2','lambda3','thetas1','thetas2','thetas3','thetar1','thetar2','thetar3']
        for variable in soilVars1: vars(self.var)[variable] = []


        i = 0
        for coverType in self.var.coverTypes[:2]:
            if i==0:
                pre = coverType + "_"
            else:
                pre = ""
            # ksat in cm/d-1 -> m/dm
            self.var.KSat1.append((loadmap(pre + "KSat1"))/100)
            self.var.KSat2.append((loadmap(pre + "KSat2"))/100)
            self.var.KSat3.append((loadmap(pre + "KSat3"))/100)
            self.var.alpha1.append((loadmap(pre + "alpha1")))
            self.var.alpha2.append((loadmap(pre + "alpha2")))
            self.var.alpha3.append((loadmap(pre + "alpha3")))
            self.var.lambda1.append((loadmap(pre + "lambda1")))
            self.var.lambda2.append((loadmap(pre + "lambda2")))
            self.var.lambda3.append((loadmap(pre + "lambda3")))
            self.var.thetas1.append((loadmap(pre + "thetas1")))
            self.var.thetas2.append((loadmap(pre + "thetas2")))
            self.var.thetas3.append((loadmap(pre + "thetas3")))
            self.var.thetar1.append((loadmap(pre + "thetar1")))
            self.var.thetar2.append((loadmap(pre + "thetar2")))
            self.var.thetar3.append((loadmap(pre + "thetar3")))
            i += 1



        # Van Genuchten n and m coefficients
        # GenuN1=Lambda+1
        with np.errstate(invalid='ignore', divide='ignore'):
            genuN1 = [x + 1 for x in self.var.lambda1]
            genuN2 = [x + 1 for x in self.var.lambda2]
            genuN3 = [x + 1 for x in self.var.lambda3]
            # self.var.GenuM1=Lambda1/GenuN1
            self.var.genuM1 = [x / y for x, y in zip(self.var.lambda1, genuN1)]
            self.var.genuM2 = [x / y for x, y in zip(self.var.lambda2, genuN2)]
            self.var.genuM3 = [x / y for x, y in zip(self.var.lambda3, genuN3)]
            # self.var.GenuInvM1=1/self.var.GenuM1
            self.var.genuInvM1 = [1 / x for x in self.var.genuM1]
            self.var.genuInvM2 = [1 / x for x in self.var.genuM2]
            self.var.genuInvM3 = [1 / x for x in self.var.genuM3]
            # self.var.GenuInvN1=1/GenuN1
            self.var.genuInvN1 = [1 / x for x in genuN1]
            self.var.genuInvN2 = [1 / x for x in genuN2]
            self.var.genuInvN3 = [1 / x for x in genuN3]
            # InvAlpha1=1/Alpha1
            self.var.invAlpha1 = [1 / x for x in self.var.alpha1]
            self.var.invAlpha2 = [1 / x for x in self.var.alpha2]
            self.var.invAlpha3 = [1 / x for x in self.var.alpha3]


        soilVars2 = ['ws1','ws2','ws3','wres1','wres2','wres3','wrange1','wrange2','wrange3','wfc1','wfc2','wfc3','wwp1','wwp2','wwp3','kunSatFC12','kunSatFC23']
        for variable in soilVars2: vars(self.var)[variable] = []

        i = 0
        for coverType in self.var.coverTypes[:4]:
            j = 0
            if coverType != "forest": j = 1
            self.var.ws1.append(self.var.thetas1[j] * self.var.rootDepth[0][i])
            self.var.ws2.append(self.var.thetas2[j] * self.var.rootDepth[1][i])
            self.var.ws3.append(self.var.thetas3[j] * self.var.rootDepth[2][i])

            self.var.wres1.append(self.var.thetar1[j] * self.var.rootDepth[0][i])
            self.var.wres2.append(self.var.thetar2[j] * self.var.rootDepth[1][i])
            self.var.wres3.append(self.var.thetar3[j] * self.var.rootDepth[2][i])

            self.var.wrange1.append(self.var.ws1[i] - self.var.wres1[i])
            self.var.wrange2.append(self.var.ws2[i] - self.var.wres2[i])
            self.var.wrange3.append(self.var.ws3[i] - self.var.wres3[i])

            # Soil moisture at field capacity (pF2, 100 cm) [mm water slice]    # Mualem equation (van Genuchten, 1980)
            self.var.wfc1.append(self.var.wres1[i] + self.var.wrange1[i] / ((1 + (self.var.alpha1[j] * 100) ** genuN1[j]) ** self.var.genuM1[j]))
            self.var.wfc2.append(self.var.wres2[i] + self.var.wrange2[i] / ((1 + (self.var.alpha2[j] * 100) ** genuN2[j]) ** self.var.genuM2[j]))
            self.var.wfc3.append(self.var.wres3[i] + self.var.wrange3[i] / ((1 + (self.var.alpha3[j] * 100) ** genuN3[j]) ** self.var.genuM3[j]))

            # Soil moisture at wilting point (pF4.2, 10**4.2 cm) [mm water slice]    # Mualem equation (van Genuchten, 1980)
            self.var.wwp1.append(self.var.wres1[i] + self.var.wrange1[i] / ((1 + (self.var.alpha1[j] * (10**4.2)) ** genuN1[j]) ** self.var.genuM1[j]))
            self.var.wwp2.append(self.var.wres2[i] + self.var.wrange2[i] / ((1 + (self.var.alpha2[j] * (10**4.2)) ** genuN2[j]) ** self.var.genuM2[j]))
            self.var.wwp3.append(self.var.wres3[i] + self.var.wrange3[i] / ((1 + (self.var.alpha3[j] * (10**4.2)) ** genuN3[j]) ** self.var.genuM3[j]))



            satTerm1FC = np.maximum(0., self.var.wfc1[i] - self.var.wres1[i]) / self.var.wrange1[i]
            satTerm2FC = np.maximum(0., self.var.wfc2[i] - self.var.wres2[i]) / self.var.wrange2[i]
            satTerm3FC = np.maximum(0., self.var.wfc3[i] - self.var.wres3[i]) / self.var.wrange3[i]
            kUnSat1FC = self.var.KSat1[j] * np.sqrt(satTerm1FC) * np.square(1 - (1 - satTerm1FC ** self.var.genuInvM1[j]) ** self.var.genuM1[j])
            kUnSat2FC = self.var.KSat2[j] * np.sqrt(satTerm2FC) * np.square(1 - (1 - satTerm2FC ** self.var.genuInvM2[j]) ** self.var.genuM2[j])
            self.var.kUnSat3FC = self.var.KSat3[j] * np.sqrt(satTerm3FC) * np.square(1 - (1 - satTerm3FC ** self.var.genuInvM3[j]) ** self.var.genuM3[j])
            self.var.kunSatFC12.append(np.sqrt(kUnSat1FC * kUnSat2FC))
            self.var.kunSatFC23.append(np.sqrt(kUnSat2FC * self.var.kUnSat3FC))

            i += 1



        i = 0
        for coverType in self.var.coverTypes[:4]:
            # other paramater values
            # b coefficient of soil water storage capacity distribution
            #self.var.minTopWaterLayer.append(loadmap(coverType + "_minTopWaterLayer"))
            #self.var.minCropKC.append(loadmap(coverType + "_minCropKC"))

            #self.var.minInterceptCap.append(loadmap(coverType + "_minInterceptCap"))
            #self.var.cropDeplFactor.append(loadmap(coverType + "_cropDeplFactor"))
            # parameter values

            self.var.rootFraction1.append(loadmap(coverType + "_rootFraction1"))
            #self.var.rootFraction2 = self.var.rootFraction1
            self.var.maxRootDepth.append(loadmap(coverType + "_maxRootDepth"))

            # store filenames
            self.var.cropCoefficientNC_filename.append(coverType + "_cropCoefficientNC")
            self.var.interceptCapNC_filename.append(coverType + "_interceptCapNC")
            self.var.coverFractionNC_filename.append(coverType + "_coverFractionNC")


            # init values
            #self.var.interflow[i] = self.var.load_initial(coverType + "_interflow")
            self.var.w1[i] = self.var.load_initial(coverType + "_w1",default = self.var.wwp1[i])
            self.var.w2[i] = self.var.load_initial(coverType + "_w2",default = self.var.wwp2[i])
            self.var.w3[i] = self.var.load_initial(coverType + "_w3",default = self.var.wwp3[i])

            soilVars = ['w1', 'w2', 'w3']
            for variable in soilVars:
                vars(self.var)["sum_" + variable] = globals.inZero.copy()
                for No in range(4):
                    vars(self.var)["sum_" + variable] += self.var.fracVegCover[No] * vars(self.var)[variable][No]

            # for paddy irrigation flooded paddy fields
            self.var.topwater = self.var.load_initial("topwater", default= 0.) * globals.inZero.copy()
            self.var.sum_topwater = self.var.fracVegCover[2] * self.var.topwater
            self.var.sum_soil = self.var.sum_w1 + self.var.sum_w2 + self.var.sum_w3 + self.var.sum_topwater
            self.var.totalSto = self.var.SnowCover + self.var.sum_interceptStor + self.var.sum_soil

            # Improved Arno's scheme parameters: Hageman and Gates 2003
            # arnoBeta defines the shape of soil water capacity distribution curve as a function of  topographic variability
            # b = max( (oh - o0)/(oh + omax), 0.01)
            # oh: the standard deviation of orography, o0: minimum std dev, omax: max std dev

            self.var.arnoBetaOro = (self.var.ElevationStD - 10.0) / (self.var.ElevationStD + 1500.0)

            # for CALIBRATION
            self.var.arnoBetaOro = self.var.arnoBetaOro + loadmap('arnoBeta_add')
            self.var.arnoBetaOro = np.minimum(1.2, np.maximum(0.01, self.var.arnoBetaOro))

            self.var.arnoBeta[i] = self.var.arnoBetaOro + loadmap(coverType + "_arnoBeta")
            self.var.arnoBeta[i] = np.minimum(1.2, np.maximum(0.01, self.var.arnoBeta[i]))

            # Due to large rooting depths, the third (final) soil layer may be pushed to its minimum of 0.05 m.
            # In such a case, it may be better to turn off the root fractioning feature, as there is limited depth
            # in the third soil layer to hold water, while having a significant fraction of the rootss.
            # TODO: Extend soil depths to match maximum root depths
            
            rootFrac = np.tile(globals.inZero,(self.var.soilLayers,1))
            fractionroot12 = self.var.rootDepth[0][i] / (self.var.rootDepth[0][i] + self.var.rootDepth[1][i] )
            rootFrac[0] = fractionroot12 * self.var.rootFraction1[i]
            rootFrac[1] = (1 - fractionroot12) * self.var.rootFraction1[i]
            rootFrac[2] = 1.0 - self.var.rootFraction1[i]

            if 'rootFrac' in binding:
                if not checkOption('rootFrac'):
                    root_depth_sum = self.var.rootDepth[0][i] + self.var.rootDepth[1][i] + self.var.rootDepth[2][i]
                    for layer in range(3):
                        rootFrac[layer] = self.var.rootDepth[layer][i] / root_depth_sum

            rootFracSum = np.sum(rootFrac,axis=0)

            for soilLayer in range(self.var.soilLayers):
                self.var.adjRoot[soilLayer][i] = rootFrac[soilLayer] / rootFracSum
            i += 1




        # for maximum of topwater flooding (default = 0.05m)
        self.var.maxtopwater = 0.05
        if "irrPaddy_maxtopwater" in binding:
            self.var.maxtopwater = loadmap('irrPaddy_maxtopwater')


        #self.var.landcoverSumSum = ['directRunoff', 'totalPotET', 'potTranspiration', "Precipitation", 'ETRef','gwRecharge','Runoff']
        #for variable in self.var.landcoverSumSum:
        #    vars(self.var)["sumsum_" + variable] = globals.inZero.copy()

        # for irrigation of non paddy -> No =3
        totalWaterPlant1 = np.maximum(0., self.var.wfc1[3] - self.var.wwp1[3]) #* self.var.rootDepth[0][3]
        totalWaterPlant2 = np.maximum(0., self.var.wfc2[3] - self.var.wwp2[3]) #* self.var.rootDepth[1][3]
        #totalWaterPlant3 = np.maximum(0., self.var.wfc3[3] - self.var.wwp3[3]) * self.var.rootDepth[2][3]
        self.var.totAvlWater = totalWaterPlant1 + totalWaterPlant2 #+ totalWaterPlant3

    # --------------------------------------------------------------------------

    def dynamic_fracIrrigation(self, init = False, dynamic = True):
        """
        Dynamic part of the land cover type module

        Calculating fraction of land cover

        * loads the fraction of landcover for each year from netcdf maps
        * calculate the fraction of 6 land cover types based on the maps

        :param init: (optional) True: set for the first time of a run
        :param dynamic: used in the dynmic run not in the initial phase
        :return: -

        """

        #if checkOption('includeIrrigation') and checkOption('dynamicIrrigationArea'):

        # updating fracVegCover of landCover (for historical irrigation areas, done at yearly basis)
        # if first day of the year or first day of run

        if init and dynamic:

            if self.var.dynamicLandcover:
                landcoverYear = dateVar['currDate']
            else:
                landcoverYear = datetime.datetime(int(binding['fixLandcoverYear']), 1, 1)

            i = 0


            for coverType in self.var.coverTypes:
                
                self.var.fracVegCover[i] = readnetcdf2('fractionLandcover', landcoverYear, useDaily="yearly",  value= 'frac'+coverType)
                i += 1


            # for Xiaogang's agent model
            if "paddyfraction" in binding:
                self.var.fracVegCover[2] = loadmap('paddyfraction')
                self.var.fracVegCover[3] = loadmap('nonpaddyfraction')


            # correction of grassland if sum is not 1.0
            sum = np.sum(self.var.fracVegCover,axis=0)
            self.var.fracVegCover[1] = np.maximum(0.,self.var.fracVegCover[1] + 1.0 - sum)
            sum = np.sum(self.var.fracVegCover, axis=0)
            self.var.fracVegCover[0] = np.maximum(0., self.var.fracVegCover[0] + 1.0 - sum)
            sum = np.sum(self.var.fracVegCover,axis=0)

            # sum of landcover without water and sealed
            # self.var.sum_fracVegCover = np.sum(self.var.fracVegCover[0:4], axis=0)

            # if irrigation is off every fraction of paddy and non paddy irrigation is put to land dcover 'grassland'
            if not(checkOption('includeIrrigation')):
                self.var.fracVegCover[1] = self.var.fracVegCover[1] + self.var.fracVegCover[2] + self.var.fracVegCover[3]
                self.var.fracVegCover[2] = 0.0
                self.var.fracVegCover[3] = 0.0





            #self.var.fracVegCover[0] = self.var.fracVegCover[0] + self.var.fracVegCover[4]
            #self.var.fracVegCover[1] = self.var.fracVegCover[1] + self.var.fracVegCover[5]
            """
            self.var.fracVegCover[0] = 0.2   # forest
            self.var.fracVegCover[1] = 0.2  # others (grassland)
            self.var.fracVegCover[2] = 0.2  # paddy irrigation
            self.var.fracVegCover[3] = 0.2  # non paddy irrigation
            self.var.fracVegCover[4] = 0.1
            self.var.fracVegCover[5] = 0.1
            """


# --------------------------------------------------------------------------

    def dynamic(self):
        """
        Dynamic part of the land cover type module

        Calculating soil for each of the 6  land cover class

        * calls evaporation_module.dynamic
        * calls interception_module.dynamic
        * calls soil_module.dynamic
        * calls sealed_water_module.dynamic

        And sums every thing up depending on the land cover type fraction
        """

        #if (dateVar['curr'] == 15):
        #    ii=1

        if checkOption('calcWaterBalance'):
            preIntStor = self.var.sum_interceptStor.copy()
            preStor1 = self.var.sum_w1.copy()
            preStor2 = self.var.sum_w2.copy()
            preStor3 = self.var.sum_w3.copy()
            pretop = self.var.sum_topwater

        ### To compute water balance for modflow
        if self.var.modflow:
            if (dateVar['curr'] - int(dateVar['curr'] / self.var.modflow_timestep) * self.var.modflow_timestep) == 1 and \
                    dateVar['curr'] > self.var.modflow_timestep:  # if it is the first step of the week
                self.var.presumed_sum_gwRecharge = self.var.sumed_sum_gwRecharge.copy()
                # stormodf = np.nansum((self.var.presumed_sum_gwRecharge/self.var.modflow_timestep-self.var.capillar-self.var.baseflow) * self.var.cellArea) # From ModFlow during the previous step
                # stormodf = self.var.GWVolumeVariation / self.var.modflow_timestep # GW volume change from the previous ModFlow run (difference betwwen water levels times porosity)
        self.var.pretotalSto = self.var.totalSto.copy()

        coverNo = 0
        # update soil (loop per each land cover type):
        for coverType in self.var.coverTypes:
            if checkOption('includeIrrigation'):
                usecovertype = 4  # include paddy and non paddy irrigation
            else:
                usecovertype = 2   # exclude irrigation
            # calculate evaporation and transpiration for soil land cover types (not for sealed and water covered areas)
            if coverNo < usecovertype:
                self.model.evaporation_module.dynamic(coverType, coverNo)
            self.model.interception_module.dynamic(coverType, coverNo)
            coverNo += 1

        # -----------------------------------------------------------
        # Calculate  water available for infiltration
        # *********  WATER Demand   *************************
        self.model.waterdemand_module.dynamic()

        # Calculate soil
        coverNo = 0
        for coverType in self.var.coverTypes:
            if checkOption('includeIrrigation'):
                usecovertype = 4  # include paddy and non paddy irrigation
            else:
                usecovertype = 2   # exclude irrgation

            if coverNo < usecovertype:
                self.model.soil_module.dynamic(coverType, coverNo)
            if coverNo > 3:
                # calculate for openwater and sealed area
                self.model.sealed_water_module.dynamic(coverType, coverNo)
            coverNo += 1


        # aggregated variables by fraction of land cover
        for variable in self.var.landcoverSum:
            vars(self.var)["sum_" + variable] = globals.inZero.copy()
            for No in range(6):
                vars(self.var)["sum_" + variable] += self.var.fracVegCover[No] * vars(self.var)[variable][No]

        #print "--", self.var.sum_directRunoff



        soilVars = ['w1','w2','w3']
        for variable in soilVars:
                vars(self.var)["sum_" + variable] = globals.inZero.copy()
                for No in range(4):
                    vars(self.var)["sum_" + variable] += self.var.fracVegCover[No] * vars(self.var)[variable][No]



        self.var.sum_topwater = self.var.fracVegCover[2] * self.var.topwater
        self.var.totalET = self.var.sum_actTransTotal + self.var.sum_actBareSoilEvap + self.var.sum_openWaterEvap + self.var.sum_interceptEvap + self.var.snowEvap + self.var.addtoevapotrans
        # addtoevapotrans: part of water demand which is lost due to evaporation
        self.var.sum_soil = self.var.sum_w1 + self.var.sum_w2 + self.var.sum_w3 + self.var.sum_topwater
        self.var.totalSto = self.var.SnowCover + self.var.sum_interceptStor + self.var.sum_soil
        self.var.sum_runoff = self.var.sum_directRunoff + self.var.sum_interflow

        ### Printing the soil+GW water balance (considering no pumping), without the surface part
        #print('Date : ', dateVar['currDatestr'])
        if checkOption('calcWaterBalance'):
            if self.var.modflow:
                if dateVar['curr'] > self.var.modflow_timestep:  # from the second step
                    storcwat = np.sum((self.var.totalSto - self.var.pretotalSto) * self.var.cellArea)  # Daily CWAT storage variations
                    cwatbudg = np.sum((self.var.Precipitation - self.var.sum_runoff - self.var.totalET + self.var.presumed_sum_gwRecharge / self.var.modflow_timestep - self.var.sum_gwRecharge - self.var.baseflow) * self.var.cellArea)  # Inputs-Outputs (baseflow comes from the previous ModFlow model)
                    print('CWatM-ModFlow water balance error [%]: ',
                          round(100 * (cwatbudg - storcwat - self.var.GWVolumeVariation / self.var.modflow_timestep) /
                                (0.5 * cwatbudg + 0.5 * storcwat + 0.5 * self.var.GWVolumeVariation / self.var.modflow_timestep) * 100) / 100)

        # --------------------------------------------------------------------

        #if (dateVar['curr'] == 104):
        #    ii=1

        if checkOption('calcWaterBalance'):
            self.model.waterbalance_module.waterBalanceCheck(
                [self.var.Rain,self.var.SnowMelt],  # In
                [self.var.sum_availWaterInfiltration,self.var.sum_interceptEvap],  # Out
                [preIntStor],   # prev storage
                [self.var.sum_interceptStor],
                "InterAll", False)


        if checkOption('calcWaterBalance'):
            self.model.waterbalance_module.waterBalanceCheck(
                [self.var.sum_availWaterInfiltration,self.var.sum_capRiseFromGW, self.var.sum_act_irrConsumption],       # In
                [self.var.sum_directRunoff,self.var.sum_perc3toGW, self.var.sum_prefFlow,
                 self.var.sum_actTransTotal, self.var.sum_actBareSoilEvap,self.var.sum_openWaterEvap],             # Out
                [pretop,preStor1,preStor2,preStor3],                                                      # prev storage
                [self.var.sum_w1, self.var.sum_w2, self.var.sum_w3,self.var.sum_topwater],
                "Soil_sum1", False)

        if checkOption('calcWaterBalance'):
            self.model.waterbalance_module.waterBalanceCheck(
                [self.var.Rain,self.var.SnowMelt, self.var.sum_act_irrConsumption],                             # In
                [self.var.sum_directRunoff,self.var.sum_interflow,self.var.sum_gwRecharge,
                 self.var.sum_actTransTotal, self.var.sum_actBareSoilEvap,self.var.sum_openWaterEvap,self.var.sum_interceptEvap],  # Out
                [pretop,preStor1,preStor2,preStor3,preIntStor],                                       # prev storage
                [self.var.sum_w1, self.var.sum_w2, self.var.sum_w3,self.var.sum_interceptStor,self.var.sum_topwater],
                "Soil_sum111", False)



        if checkOption('calcWaterBalance'):
            self.model.waterbalance_module.waterBalanceCheck(
                [self.var.Precipitation, self.var.sum_act_irrConsumption],                             # In
                [self.var.sum_directRunoff,self.var.sum_interflow,self.var.sum_gwRecharge,
                 self.var.sum_actTransTotal, self.var.sum_actBareSoilEvap,self.var.sum_openWaterEvap,self.var.sum_interceptEvap,self.var.snowEvap],  # Out
                [pretop,preStor1,preStor2,preStor3,preIntStor,self.var.prevSnowCover],                                       # prev storage
                [self.var.sum_w1, self.var.sum_w2, self.var.sum_w3,self.var.sum_interceptStor,self.var.SnowCover,self.var.sum_topwater],
                "Soil_sum2", False)

        if checkOption('calcWaterBalance'):
            self.model.waterbalance_module.waterBalanceCheck(
                [self.var.Precipitation, self.var.sum_act_irrConsumption],                             # In
                [self.var.sum_directRunoff,self.var.sum_interflow,self.var.sum_gwRecharge,
                 self.var.sum_actTransTotal, self.var.sum_actBareSoilEvap, self.var.sum_openWaterEvap, self.var.sum_interceptEvap, self.var.snowEvap],   # Out
                [self.var.pretotalSto],                                       # prev storage
                [self.var.totalSto],
                "Soil_sum2b", False)



        if checkOption('calcWaterBalance'):
            self.model.waterbalance_module.waterBalanceCheck(
                [self.var.Precipitation,self.var.act_irrWithdrawal],                             # In
                [self.var.sum_directRunoff,self.var.sum_interflow,self.var.sum_gwRecharge,
                 self.var.totalET,self.var.act_nonIrrConsumption,self.var.returnFlow ],                   # Out
                [self.var.pretotalSto],                                       # prev storage
                [self.var.totalSto],
                "Soil_sum3", False)  #  -> something wrong

        if checkOption('calcWaterBalance'):
            self.model.waterbalance_module.waterBalanceCheck(
                [self.var.Precipitation],                             # In
                [self.var.sum_runoff,self.var.sum_gwRecharge,self.var.totalET ],  # out
                [self.var.pretotalSto],                                       # prev storage
                [self.var.totalSto],
                "Soil_sum4", False)




        #[self.var.waterWithdrawal],  # In
        #[self.var.sumirrConsumption, self.var.returnFlow, self.var.addtoevapotrans, nonIrruse],  # Out


        #a = decompress(self.var.sumsum_Precipitation)
        #b = cellvalue(a,81,379)
        #print self.var.sum_directRunoff
        #report(decompress(self.var.sumsum_Precipitation), "c:\work\output\Prsum.map")
        #report(decompress(self.var.sumsum_gwRecharge), "c:\work\output\gwrsum.map")
        
