describe("Django REST framework / React quickstart app", () => {
    const player = {
      name: "Julius Junior Kazibwe",
      email: "kazibwejuliusjunior@gmail.com",
      message: "I am looking for a React tutor"
    };
    before(() => {
      cy.exec("npm run dev");
      cy.exec("npm run flush");
    });
    it("should be able to fill a web form", () => {
      cy.visit("/");
      cy
        .get('input[name="name"]')
        .type(player.name)
        .should("have.value", player.name);
      cy
        .get('input[name="email"]')
        .type(player.email)
        .should("have.value", player.email);
      cy
        .get('textarea[name="message"]')
        .type(player.message)
        .should("have.value", player.message);
      cy.get("form").submit();
    });
    // more tests here
    it("should be able to see the table", () => {
        cy.visit("/");
        cy.get("tr").contains(`${player.name}${player.email}${player.message}`);
      });
  });