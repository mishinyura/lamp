async function request(path='/', method='GET', body={}) {
  try {
    setting = {
        method: method
    }

    if (method === 'POST') {
        setting.body = JSON.stringify(body)
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
}

main()