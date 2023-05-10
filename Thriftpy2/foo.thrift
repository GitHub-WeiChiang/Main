service PingPong{
    string ping(),
    string login(
        1: string username,
        2: string password
    )
}
