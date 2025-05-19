async function request(path='/', method='GET', data={}) {
  try {
    setting = {
        method: method
    }

    if (method === 'POST') {
        setting.data = data
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

// Вызов функции
async function main() {
    let data = await request('http://localhost:8000/orders')
    console.log(data)
}

main()