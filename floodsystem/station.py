"""This module provides a model for a monitoring station, and tools
for manipulating/modifying station data

"""


class MonitoringStation:
    """This class represents a river level monitoring station"""

    def __init__(self, station_id, measure_id, label, coord, typical_range,
                 river, town):

        self.station_id = station_id
        self.measure_id = measure_id

        # Handle case of erroneous data where data system returns
        # '[label, label]' rather than 'label'
        self.name = label
        if isinstance(label, list):
            self.name = label[0]

        self.coord = coord
        self.typical_range = typical_range
        self.river = river
        self.town = town

        self.latest_level = None

    def __repr__(self):
        d = "Station name:     {}\n".format(self.name)
        d += "   id:            {}\n".format(self.station_id)
        d += " measure id: {}\n".format(self.measure_id)
        d += "   coordinate:    {}\n".format(self.coord)
        d += "   town:          {}\n".format(self.town)
        d += "   river:         {}\n".format(self.river)
        d += "   typical range: {}\n".format(self.typical_range)
        d += '   latest_level: {}'.format(self.latest_level);
        return d

    def relative_water_level(self):
        '''
             returns the latest water level as a fraction of the typical range. if data is not available, None is returned
        '''        
        if self.typical_range != None and self.latest_level != None:
            range_span = abs(self.typical_range[1] - self.typical_range[0]);

            # latest_level can sometimes be an array
            try:
                relative_level = ( self.latest_level - self.typical_range[0] ) / range_span;
            except:
                relative_level = ( self.latest_level[0] - self.typical_range[0] ) / range_span;
            finally:
                return relative_level;
        else:
            return None;
    
    def typical_range_consistent(self):
        '''
            return ture if the typical range of station is consistent, return false if not consistent or data not available.
        '''
        if self.typical_range == None:
            return False
            #return false if data not avaiable
        elif self.typical_range[0] < self.typical_range[1]:
            #return true if range is consistent
            return True
        else:
            return False
            #for other situation, return false

def inconsistent_typical_range_stations(stations):
    """
        ruturns a list of inconsistent stations.
    """
    inconsistent_list = []
    for station in stations:
        if MonitoringStation.typical_range_consistent(station) == False:
            inconsistent_list.append(station.name)
            #add the station to the list if the consistent test failed
    inconsistent_list = sorted(inconsistent_list)
    #sort the inconsistent list
    return inconsistent_list
            