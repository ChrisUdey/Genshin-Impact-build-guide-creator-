describe('Home Page', () => {
    it('should display characters on home page', () => {
        cy.visit('/');
        cy.get('a[href^="/characters/"]').should('have.length', 4);
    });

    it('should navigate through pagination', () => {
        cy.visit('/');
        cy.get('button').filter(':visible').last().click();
        cy.wait(500);
    });

    it('should navigate to character detail', () => {
        cy.visit('/');
        cy.get('a[href^="/characters/"]').first().click();
        cy.url().should('include', '/characters/');
    });

    it('should fail if API server is not running', () => {
        cy.visit('/');
        cy.get('a[href^="/characters/"]', { timeout: 5000 }).should('have.length.at.least', 1);
    });
});
