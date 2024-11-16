<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Femminder</title>
    <style>
        body {
            font-family: Arial, sans-serif;
            margin: 0;
            padding: 0;
            background-color: #f8f1f4;
            display: flex;
            justify-content: center;
            align-items: center;
            height: 100vh;
        }
        .container {
            text-align: center;
            background: white;
            padding: 30px;
            border-radius: 15px;
            box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
            width: 90%;
            max-width: 400px;
        }
        .container h1 {
            font-size: 1.8rem;
            color: #d32276;
            margin-bottom: 20px;
        }
        .container p {
            color: #555;
            margin-bottom: 20px;
        }
        .roles {
            display: flex;
            justify-content: space-around;
            margin-bottom: 20px;
        }
        .role {
            cursor: pointer;
            text-align: center;
            padding: 10px;
            background: #f8f8f8;
            border: 2px solid transparent;
            border-radius: 10px;
            transition: border-color 0.3s ease;
        }
        .role:hover {
            border-color: #d32276;
        }
        .role img {
            width: 60px;
            height: 60px;
            margin-bottom: 10px;
        }
        .role span {
            display: block;
            font-size: 1rem;
            color: #333;
        }
        .btn-next {
            display: inline-block;
            padding: 10px 20px;
            background: #d32276;
            color: white;
            border: none;
            border-radius: 20px;
            font-size: 1rem;
            text-decoration: none;
            cursor: pointer;
            transition: background 0.3s ease;
        }
        .btn-next:hover {
            background: #b71f62;
        }
    </style>
</head>
<body>
    <div class="container">
        <h1>Hello <span style="color: #d32276;">Femminder</span> Friends, Welcome!</h1>
        <p>Choose a role to start the application!</p>
        <div class="roles">
            <div class="role">
                <img src="https://via.placeholder.com/60?text=Admin" alt="Admin">
                <span>Admin</span>
            </div>
            <div class="role">
                <img src="https://via.placeholder.com/60?text=User" alt="User">
                <span>User</span>
            </div>
        </div>
        <a href="#" class="btn-next">Next</a>
    </div>
</body>
</html>
