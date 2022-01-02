# CICDPipeline

:::mermaid
classDiagram
    class BankAccount
    BankAccount : +String owner
    BankAccount : +Bigdecimal balance
    BankAccount : +deposit(amount) bool
    BankAccount : +withdrawl(amount) int
    vehicle <|-- car 
::: 
