async function request(path='/', method='GET', body={}) {
  try {
    setting = {
        method: method
    }

    if (method === 'POST') {
        setting.body = JSON.stringify(body)
        setting.headers = {'Content-Type': 'application/json'}
    }
    const response = await fetch(path, setting);
    if (!response.ok) {
        throw new Error(`HTTP error! Status: ${response.status}`);
    }
    const data = await response.json()
    return data;
  } catch (error) {
    console.error('Ошибка:', error);
  }
}


function print(data) {
    console.log(data)
}