MAIN_MESSAGES = {
    "en": {
        #get_autobuy_data
        "get_autobuy_data_try_request": "Request for {}",
        "get_autobuy_data_success_response": "Successful response for {}",
        "get_autobuy_data_http_error": "HTTP Error {} for {}",
        "get_autobuy_data_http_status_error": "HTTP Error Status while parsing histogram: {}",
        "get_autobuy_data_request_error": "Request Error while parsing histogram: {}",
        "get_autobuy_data_proxy_error": "Proxy Error while parsing histogram: {}",

        #get_history_data
        "get_history_data_try_request": "Request for {}",
        "get_history_data_success_response": "Successful response for {}",
        "get_history_data_skip_boosted": "Item skipped because boosted",
        "get_history_data_http_error": "HTTP Error {} for {}",
        "get_history_data_http_status_error": "HTTP Error Status while parsing histogram: {}",
        "get_history_data_request_error": "Request Error while parsing histogram: {}",
        "get_history_data_proxy_error": "Proxy Error while parsing histogram: {}",

        #fetch_market_data
        "fetch_market_data_try_request": "Request for {}",
        "fetch_market_data_success_response": "Successful response from {}",
        "fetch_market_item_not_found": "Item {} not found",
        "fetch_market_http_error": "HTTP Error {} for {}",
        "fetch_market_request_error": "Request Error for {}: {}",

        #process_autobuy_json_to_data
        "process_autobuy_json_to_data_json_unsuccessful": "JSON is empty or success == False for Autobuy response",
        "process_autobuy_json_to_data_key_error": "Error processing JSON: {}",

        #process_autosearch_json_to_data
        "process_autosearch_json_to_data_json_unsuccessful": "success == false or JSON is empty in process_autosearch_json_to_data",
        "process_autosearch_json_to_data_no_buyers": "No one is buying this item(Parameter sell_order_price == None)",
        "process_autosearch_json_to_data_no_sellers": "No one is selling this item(Parameter buy_order_price == None)",
        "process_autosearch_json_to_data_less_profit": "Difference {}% < {}% item skipped",
        "process_autosearch_json_to_data_less_sales": "Sales {} < {} item skipped",
        "process_autosearch_json_to_data_key_error": "Error processing JSON: {}",

        # process_main_json_to_data
        "process_main_json_to_data_json_unsuccessful": "JSON is empty in process_main_json_to_data",
        "process_main_json_to_data_no_buyers": "Parameter buy_order_price is null",
        "process_main_json_to_data_item_not_listed": "Item ({}) is not listed on the marketplace",
        "process_main_json_to_data_key_error": "Error processing JSON: {}",

        # fetch_and_process
        "fetch_and_process_data_not_retrieved": "Error: data for {} not retrieved",

    },
    "ru": {
        #get_autobuy_data
        "get_autobuy_data_try_request": "Запрос на {}",
        "get_autobuy_data_success_response": "Успешный запрос на {}",
        "get_autobuy_data_http_error": "Ошибка HTTP {} для {}",
        "get_autobuy_data_http_status_error": "HTTP ошибка при получении данных из histogram: {}",
        "get_autobuy_data_request_error": "Сетевая ошибка при получении данных из histogram: {}",
        "get_autobuy_data_proxy_error": "Ошибка прокси при получении данных из histogram: {}",

        #get_history_data
        "get_history_data_try_request": "Запрос на {}",
        "get_history_data_success_response": "Успешный запрос на {}",
        "get_history_data_skip_boosted": "Предмет пропущен т.к. забущен",
        "get_history_data_http_error": "Ошибка HTTP {} для {}",
        "get_history_data_http_status_error": "HTTP ошибка при получении данных из histogram: {}",
        "get_history_data_request_error": "Сетевая ошибка при получении данных из histogram: {}",
        "get_history_data_proxy_error": "Ошибка прокси при получении данных из histogram: {}",

        #fetch_market_data
        "fetch_market_data_try_request": "Запрос на {}",
        "fetch_market_data_success_response": "Успешный запрос на {}",
        "fetch_market_item_not_found": "Скин {} не найден",
        "fetch_market_http_error": "Ошибка HTTP {} для {}",
        "fetch_market_request_error": "Сетевая ошибка для {}: {}",

        #process_autobuy_json_to_data
        "process_autobuy_json_to_data_json_unsuccessful": "JSON или пуст или success == False для запроса по автопокупке",
        "process_autobuy_json_to_data_key_error": "Ошибка обработки JSON: {}",

        #process_autosearch_json_to_data
        "process_autosearch_json_to_data_json_unsuccessful": "success == false или JSON пуст в process_autosearch_json_to_data",
        "process_autosearch_json_to_data_no_buyers": "Никто не покупает данный предмет(Параметр sell_order_price == None)",
        "process_autosearch_json_to_data_no_sellers": "Никто не продает данный предмет(Параметр buy_order_price == None)",
        "process_autosearch_json_to_data_less_profit": "Разность {}% < {}% предмет пропущен",
        "process_autosearch_json_to_data_less_sales": "Продаж {} < {} предмет пропущен",
        "process_autosearch_json_to_data_key_error": "Ошибка обработки JSON: {}",

        # process_main_json_to_data
        "process_main_json_to_data_json_unsuccessful": "JSON пуст в process_main_json_to_data",
        "process_main_json_to_data_no_buyers": "Параметр buy_order_price равен null",
        "process_main_json_to_data_item_not_listed": "Предмет ({}) не продаётся на торговой площадке",
        "process_main_json_to_data_key_error": "Ошибка обработки JSON: {}",

        # fetch_and_process
        "fetch_and_process_data_not_retrieved": "Ошибка: данные для {} не получены",

    }
}





















HANDLERS_MESSAGES = {
    "en": {
        "start_radar_moode": "Radar Mode started",

    },
    "ru": {
        "start_radar_moode": "Radar Mode запущен",
    }
}