import asyncio
import datetime
import httpx
import os

from counters.api.models import EnergyMeasurements

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'counters.settings')

import django
django.setup()


N = 100  # Количество счетчиков для опроса
M = 5    # Периодичность в секундах

API_BASE_URL = 'http://127.0.0.1:{port}'


async def poll_meter(meter_number: int, port: int) -> None:
    """
    Опрашивает счетчик и записывает данные в базу данных.

    :param meter_number: Номер счетчика.
    :param port: Порт, по которому осуществляется запрос.
    """
    async with httpx.AsyncClient() as client:
        url = API_BASE_URL.format(port=port)
        response = await client.get(f"{url}/meter/{meter_number}")

    if response.status_code == 200:
        data = response.json()
        amps = data.get('amps')
        kilowatt = data.get('kilowatt')
        date = datetime.datetime.now()

        EnergyMeasurements.objects.create(
            number=meter_number,
            amps=amps,
            kilowatt=kilowatt,
            date=date
        )


async def main() -> None:
    """
    Основная функция для запуска опроса счетчиков.
    """
    for port in range(9000, 65001):
        tasks = []
        for meter_number in range(1, N + 1):
            task = asyncio.create_task(poll_meter(meter_number, port))
            tasks.append(task)

        await asyncio.gather(*tasks)
        await asyncio.sleep(M)

if __name__ == "__main__":
    asyncio.run(main())
