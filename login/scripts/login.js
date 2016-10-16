var LoginBox = React.createClass({
    getInitialState: function () {
        return { username: "", password: "", helpText: "", pendingResponse: false };
    },
    handleUsernameChanged: function (e) {
        this.setState({ username: e.target.value });
        if (this.state.helpText === "Username is required") {
            this.state.helpText = "";
        }
    },
    handlePasswordChanged: function (e) {
        this.setState({ password: e.target.value });
        if (this.state.helpText === "Password is required") {
            this.state.helpText = "";
        }
    },
    handleSubmit: function (e) {
        e.preventDefault();
        var username = this.state.username.trim();
        var password = this.state.password;
        if (!username) {
            this.setState({ helpText: "Username is required" });
            return;
        }
        if (!password) {
            this.setState({ helpText: "Password is required" });
            return;
        }
        this.setState({username: "", password: "", pendingResponse: true});
        $.ajax({
            url: "backend/loginstub.php",
            data: {username: username, password: password},
            method: "POST",
            dataType: 'json',
            cache: false,
            success: function (data) {
                if (data.loggedIn) {
                    this.state.helpText = "Logged in successfully";
                } else {
                    this.state.helpText = "Username or password is incorrect";
                }
                this.setState({pendingResponse: false});
            }.bind(this),
            error: function (xhr, status, err) {
                console.error(err.toString());
            }.bind(this)
        });
    },
    render: function () {
        return (
            <form className="loginForm" onSubmit={this.handleSubmit}>
                <p>{this.state.helpText}</p>
                <input
                    type="text"
                    placeholder="Username"
                    value={this.state.username}
                    onChange={this.handleUsernameChanged}
                    disabled={this.state.pendingResponse}
                    /><br></br>
                <input
                    type="text"
                    placeholder="Password"
                    value={this.state.password}
                    onChange={this.handlePasswordChanged}
                    disabled={this.state.pendingResponse}
                    /><br></br>
                <input type="submit" value="Log In" />
            </form>
        );
    }
});

ReactDOM.render(
    <LoginBox />,
    document.getElementById("content")
);