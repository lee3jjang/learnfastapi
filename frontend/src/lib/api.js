const fastapi = (
  operation,
  url,
  params,
  success_callback,
  failure_callback
) => {
  const method = operation;
  const content_type = "application/json";
  const body = JSON.stringify(params);
  let _url = import.meta.env.VITE_SERVER_URL + url;
  if (method === "get") {
    _url += "?" + new URLSearchParams(params);
  }

  let options = {
    method,
    headers: {
      "Content-Type": content_type,
    },
  };

  if (method !== "get") {
    options["body"] = body;
  }

  fetch(_url, options).then((response) => {
    if (response.status === 204) {
      // No content
      if (success_callback) {
        success_callback();
      }
      return;
    }
    response
      .json()
      .then((json) => {
        if (response.status >= 200 && response.status < 300) {
          // 200 ~ 299
          if (success_callback) {
            success_callback(json);
          }
        } else {
          if (failure_callback) {
            failure_callback(json);
          } else {
            alert(JSON.stringify(json));
          }
        }
      })
      .catch((error) => {
        alert(JSON.stringify(error));
      });
  });
};

export default fastapi;
