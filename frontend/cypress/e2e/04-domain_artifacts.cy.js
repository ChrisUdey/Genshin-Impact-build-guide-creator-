describe("Domain Detail Page", () => {
    before(() => {
        // Visit the first domain dynamically
        cy.request("http://127.0.0.1:8000/api/domains").then((res) => {
            const firstDomainId = res.body[0].id;
            cy.wrap(firstDomainId).as("domainId");
        });
    });

    beforeEach(function () {
        cy.visit(`/domains/${this.domainId}`);
    });

    it("loads the domain detail page", function () {
        cy.contains("Domain Artifacts").should("exist");
    });

    it("shows artifacts list", () => {
        cy.get("[data-cy=artifact-item]").should("have.length.greaterThan", 0);
    });

    it("artifact images load", () => {
        cy.get("[data-cy=artifact-item] img")
            .first()
            .should("be.visible");
    });

    it("has a back button", () => {
        cy.contains("Back").click({ force: true });
        cy.url().should("include", "/domains");
    });
});
