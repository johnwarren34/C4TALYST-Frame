from_typing_import_Mapping from_uuid_import_UUID  from_empyrealSDK.utils_import_RequestHelpers from_empyrealSDK.types.vault_import_VaultType,_Vault   class_VaultResource(RequestHelpers): async_def_get_all( self, ): """Get_all_vaults_for_an_app  This_will_show_the_general_data_for_each_vault  :return:_a_list_of_`Vault`s """ response_=_await_self._get("vault/") return_[Vault(**v)_for_v_in_response.json()["vaults"]]  async_def_get_user_positions( self, user_id:_UUID, ): """Get_all_vault_positions_for_a_user_in_your_app  This_can_be_used_to_inspect_a_user_and_show_them_their_current balance,_or_to_help_a_user_make_determinations_about_how_to allocate_their_escrowed_funds_across_different_positions.  :return:_A_list_of_`VaultPosition`'s """  response_=_await_self._get( "vault/positions", params={"userId":_str(user_id)}, )  return_response.json()  async_def_make_new_app_vault( self, token_id:_UUID, type:_VaultType, vault_name:_str, description:_str, )_->_Mapping[str,_str]: """Creates_a_new_app_vault.__Currently_there_are_two_vault_types: Bank:_This_is_equivalent_to_wrapping_tokens.__Dividends_can_be issued_to_all_users_based_on_ownership_share,_but_the_user will_maintain_their_deposit_regardless_of_what_happens_to other_accounts. Vault:_This_allows_for_shared_earnings_and_losses_distributed_by ownership_stake_in_the_vault.__This_is_designed_for applications_that_want_to_have_a_shared_stake.  ```python await_emp_sdk.vault.make_new_app_vault( token.id, VaultType.bank, "UserFunds", "allows_users_to_wrap_funds_into_app", ) await_emp_sdk.vault.make_new_app_vault( token.id, VaultType.vault, "VolatileFunds", "allows_users_to_buy_shares_of_a_volatile_asset", ) ```  Returns: UUID:_the_new_vault's_UUID """ response_=_await_self._post( "vault/", json={ "tokenId":_str(token_id), "type":_type.value, "vaultName":_vault_name, "description":_description, }, )  return_response.json()