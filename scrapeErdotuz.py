import luigi
import os
from datetime import datetime

class scrape_today(luigi.Task):

    def output(self):
        today = datetime.now().date().isoformat()
        return luigi.LocalTarget(f'./{today}.png')

    def run(self):
        url = "https://tuzgyujtasitilalom.nebih.gov.hu/geoserver/nebih/wms?service=WMS&version=1.1.0&request=GetMap&layers=nebih:tuzgyujtas&styles=&bbox=384000.0,32000.0,960000.0,384000.0&width=768&height=469&srs=EPSG:23700&format=image%2Fpng%3B+mode%3D8bit"
        os.system(f"wget '{url}'")
        os.system(f'mv wms* "$(date -Idate).png"')
        




if __name__ == "__main__":
    luigi.run()