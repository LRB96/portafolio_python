from datetime import datetime
import pytz

seoul_timezone = pytz.timezone("Asia/Seoul")
seoul_date = datetime.now(seoul_timezone)
f{"Seúl, Corea del Sur: "}